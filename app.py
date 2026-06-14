import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash, send_file
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Import database and helper modules
from database import get_db_connection, init_db
from ai_model import predict_crop_disease
from pdf_generator import generate_report_pdf

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'agriguard_secret_key_123')

# CORS — allow Netlify frontend to call this backend
CORS(app, origins=[os.getenv('FRONTEND_URL', '*')], supports_credentials=True)

# Session cookie config for cross-origin (Netlify ↔ Vercel)
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

# File Upload Configuration
UPLOAD_FOLDER = os.path.normpath(os.getenv('UPLOAD_FOLDER', 'static/uploads'))
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

# Helper decorator for login restrictions
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "error")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Helper decorator for admin restrictions
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            flash("Access denied. Admin permissions required.", "error")
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@app.route('/home')
def home():
    # Render home page
    return render_template('home.html')

@app.route('/detect')
def detect():
    # Render disease detection page
    return render_template('detect.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Asynchronous prediction handler
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image file uploaded.'}), 400
        
    file = request.files['image']
    selected_crop = request.form.get('crop_type', 'auto')
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No image selected.'}), 400

    # Validate file format
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        return jsonify({'status': 'error', 'message': 'Unsupported file format. Only JPG, JPEG, and PNG are allowed.'}), 400

    try:
        # Save file securely
        filename = secure_filename(f"scan_{int(datetime.now().timestamp())}{ext}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run Prediction (uses TensorFlow or fallback)
        disease_name, confidence = predict_crop_disease(filepath, selected_crop)

        # Save to database
        conn = get_db_connection()
        cursor = conn.cursor()

        user_id = session.get('user_id')

        # Insert prediction record
        cursor.execute('''
            INSERT INTO predictions (user_id, image_path, disease_name, confidence)
            VALUES (?, ?, ?, ?)
        ''', (user_id, filepath.replace('\\', '/'), disease_name, confidence))
        prediction_id = cursor.lastrowid

        # Log action in system prediction log
        ip_addr = request.remote_addr
        cursor.execute('''
            INSERT INTO prediction_logs (user_id, ip_address, disease_name, confidence)
            VALUES (?, ?, ?, ?)
        ''', (user_id, ip_addr, disease_name, confidence))

        # Retrieve disease info from database
        cursor.execute("SELECT * FROM diseases WHERE disease_name = ?", (disease_name,))
        disease_row = cursor.fetchone()
        conn.commit()
        conn.close()

        if disease_row:
            details = dict(disease_row)
        else:
            details = {
                'crop': 'Unknown',
                'description': 'No information available in database.',
                'symptoms': 'None.',
                'causes': 'None.',
                'treatment': 'None.',
                'prevention': 'None.',
                'fertilizers': 'None.',
                'pesticides': 'None.'
            }

        return jsonify({
            'status': 'success',
            'prediction_id': prediction_id,
            'disease_name': disease_name,
            'confidence': confidence,
            'details': details
        })

    except Exception as e:
        print(f"Prediction Route Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['role'] = user['role']
            flash(f"Welcome back, {user['name']}!", "success")
            if user['role'] == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        phone = request.form['phone'].strip()
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for('register'))

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if email exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            flash("Email address already registered.", "error")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        try:
            cursor.execute('''
                INSERT INTO users (name, email, phone, password, role)
                VALUES (?, ?, ?, ?, 'farmer')
            ''', (name, email, phone, hashed_password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            conn.close()
            flash(f"Error during registration: {e}", "error")
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get Scan List
    cursor.execute('''
        SELECT * FROM predictions 
        WHERE user_id = ? 
        ORDER BY prediction_date DESC
    ''', (user_id,))
    scans = [dict(row) for row in cursor.fetchall()]

    # Stats Calculation
    total_scans = len(scans)
    detected_diseases = len([s for s in scans if 'Healthy' not in s['disease_name']])
    healthy_scans = len([s for s in scans if 'Healthy' in s['disease_name']])
    healthy_pct = (healthy_scans / total_scans * 100) if total_scans > 0 else 100.0

    # Chart.js Distribution datasets
    cursor.execute('''
        SELECT disease_name, COUNT(*) as count 
        FROM predictions 
        WHERE user_id = ? 
        GROUP BY disease_name
    ''', (user_id,))
    chart_rows = cursor.fetchall()
    scan_labels = [row['disease_name'] for row in chart_rows]
    scan_counts = [row['count'] for row in chart_rows]

    conn.close()

    return render_template(
        'dashboard.html',
        total_scans=total_scans,
        detected_diseases=detected_diseases,
        healthy_pct=healthy_pct,
        history_list=scans,
        scan_labels=scan_labels,
        scan_counts=scan_counts
    )

@app.route('/delete_prediction/<int:prediction_id>', methods=['POST'])
@login_required
def delete_prediction(prediction_id):
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verify ownership before deletion
    cursor.execute("SELECT * FROM predictions WHERE id = ? AND user_id = ?", (prediction_id, user_id))
    pred = cursor.fetchone()
    
    if pred:
        # Delete file if exists
        try:
            if os.path.exists(pred['image_path']):
                os.remove(pred['image_path'])
        except Exception as e:
            print(f"Error deleting file: {e}")
            
        cursor.execute("DELETE FROM predictions WHERE id = ?", (prediction_id,))
        conn.commit()
        flash("Scan entry successfully deleted from history.", "success")
    else:
        flash("Unauthorized deletion request.", "error")
        
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        subject = request.form['subject'].strip()
        message = request.form['message'].strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO contacts (name, email, subject, message)
                VALUES (?, ?, ?, ?)
            ''', (name, email, subject, message))
            conn.commit()
            conn.close()
            flash("Thank you! Your message has been sent to our agronomy support team.", "success")
        except Exception as e:
            conn.close()
            flash(f"Error submitting message: {e}", "error")
            
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/admin')
@admin_required
def admin():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Roster of users
    cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
    users = [dict(row) for row in cursor.fetchall()]

    # Crop Disease list
    cursor.execute("SELECT * FROM diseases ORDER BY crop, disease_name")
    diseases = [dict(row) for row in cursor.fetchall()]

    # Contact messages
    cursor.execute("SELECT * FROM contacts ORDER BY created_at DESC")
    contacts = [dict(row) for row in cursor.fetchall()]

    # System Logs
    cursor.execute("SELECT * FROM prediction_logs ORDER BY timestamp DESC LIMIT 100")
    logs = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return render_template(
        'admin.html',
        users_list=users,
        diseases_list=diseases,
        contacts_list=contacts,
        logs_list=logs
    )

@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Delete user predictions first
        cursor.execute("SELECT image_path FROM predictions WHERE user_id = ?", (user_id,))
        preds = cursor.fetchall()
        for p in preds:
            if os.path.exists(p['image_path']):
                try:
                    os.remove(p['image_path'])
                except Exception:
                    pass

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        flash("Farmer account blocked and deleted successfully.", "success")
    except Exception as e:
        flash(f"Error blocking user: {e}", "error")
    finally:
        conn.close()
        
    return redirect(url_for('admin'))

@app.route('/admin/update_disease/<int:disease_id>', methods=['POST'])
@admin_required
def update_disease(disease_id):
    description = request.form['description'].strip()
    symptoms = request.form['symptoms'].strip()
    causes = request.form['causes'].strip()
    treatment = request.form['treatment'].strip()
    prevention = request.form['prevention'].strip()
    fertilizers = request.form['fertilizers'].strip()
    pesticides = request.form['pesticides'].strip()

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE diseases
            SET description = ?, symptoms = ?, causes = ?, treatment = ?, prevention = ?, fertilizers = ?, pesticides = ?
            WHERE id = ?
        ''', (description, symptoms, causes, treatment, prevention, fertilizers, pesticides, disease_id))
        conn.commit()
        flash("Disease database entry successfully updated.", "success")
    except Exception as e:
        flash(f"Error updating disease entry: {e}", "error")
    finally:
        conn.close()
        
    return redirect(url_for('admin'))

@app.route('/download_report/<int:prediction_id>')
def download_report(prediction_id):
    # Generates a PDF Report on the fly and returns file download
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Retrieve Prediction
    cursor.execute("SELECT * FROM predictions WHERE id = ?", (prediction_id,))
    pred_row = cursor.fetchone()
    
    if not pred_row:
        conn.close()
        flash("Report not found.", "error")
        return redirect(url_for('home'))

    prediction = dict(pred_row)
    
    # Retrieve Disease details
    cursor.execute("SELECT * FROM diseases WHERE disease_name = ?", (prediction['disease_name'],))
    disease_row = cursor.fetchone()
    
    # Retrieve Farmer email/name metadata
    user_name = "Guest Farmer"
    user_email = "guest@agriguard.com"
    if prediction['user_id']:
        cursor.execute("SELECT name, email FROM users WHERE id = ?", (prediction['user_id'],))
        user_row = cursor.fetchone()
        if user_row:
            user_name = user_row['name']
            user_email = user_row['email']

    conn.close()

    if not disease_row:
        flash("Crop disease metadata missing. Cannot generate PDF report.", "error")
        return redirect(url_for('home'))

    disease_details = dict(disease_row)

    # Generate PDF Report bytes stream
    pdf_buffer = generate_report_pdf(prediction, disease_details, user_name, user_email)

    safe_name = prediction['disease_name'].lower().replace(" ", "_")
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f"agriguard_report_{safe_name}_{prediction_id}.pdf",
        mimetype='application/pdf'
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have logged out successfully.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Initialize DB (creates database.db and inserts seed records)
    init_db()
    
    # Run development server
    app.run(host='0.0.0.0', port=5000, debug=True)
