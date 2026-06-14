# AgriGuard AI – Crop Disease Detector

AgriGuard AI is a modern, responsive, production-ready web application built using Python (Flask), Bootstrap 5, SQLite, and Pillow/NumPy-based Computer Vision algorithms. Designed specifically for farmers and agronomists, it provides instant diagnoses of crop diseases from leaf photos, offering symptoms, causes, treatments, and fertilizer/pesticide recommendations.

---

## Features

1. **AI Disease Detection**: Analyzes uploaded leaf photos instantly. Runs real deep learning models using TensorFlow if available, with a deterministic NumPy/Pillow color-texture analyzer fallback.
2. **User Authentication**: Secure farmer signup/login with password hashing, session management, and logout.
3. **Personalized Dashboard**: Visualizes farmer scans history, healthy crop ratio, scan distribution charts (Chart.js), and pest warnings.
4. **Farming Weather Integration**: Uses Open-Meteo API to capture location-based weather parameters and provide real-time agricultural advisories.
5. **PDF Report Generator**: Generates and downloads on-the-fly, high-fidelity PDF diagnostic summaries.
6. **Multi-Language Switcher**: Dynamic translation of the entire UI to English, Hindi (हिन्दी), and Tamil (தமிழ்).
7. **Admin Panel**: Separate portal for database editing, user management, prediction logs viewing, and contact messages reviewing.
8. **Dark Mode Toggle**: Persistent styling transitions between light and dark themes.

---

## Tech Stack
- **Backend**: Python 3.14+, Flask
- **Frontend**: HTML5, CSS3 (Vanilla + Dark Mode overrides), Bootstrap 5, JavaScript
- **Database**: SQLite 3
- **Libraries**: NumPy, Pillow, ReportLab, Requests, Werkzeug

---

## Installation & Setup

### 1. Clone & Navigate to Project Directory
Ensure Python 3.14 or later is installed.
```bash
cd "c:\Users\kangeshwaran\Documents\project 1"
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the project root. (An active `.env` file with defaults has been created for you).
```ini
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=agriguard_secret_key_123
DATABASE_PATH=agriguard.db
UPLOAD_FOLDER=static/uploads
ADMIN_EMAIL=admin@agriguard.com
ADMIN_PASSWORD=adminpassword123
```

### 4. Initialize Database
Initialize the database schemas and populate seed crop records.
```bash
python database.py
```
*Note: This creates `agriguard.db` and establishes the default admin account: `admin@agriguard.com` (password: `adminpassword123`).*

---

## Running the Application

### 1. Run Development Server
```bash
python app.py
```
The application will launch on: **`http://127.0.0.1:5000`**

### 2. Verify with Unit Tests
Execute the automated test suite.
```bash
python test_app.py
```

---

## Supported Diseases (12 Classes)
- **Tomato**: Healthy, Early Blight, Late Blight
- **Potato**: Healthy, Early Blight, Late Blight
- **Corn**: Healthy, Rust, Leaf Spot
- **Rice**: Healthy, Blast, Brown Spot

---

## Admin Portal Access
- **Email**: `admin@agriguard.com`
- **Password**: `adminpassword123`
*(Admin can update crop diseases in the database, block users, read contact forms, and review all prediction logs).*

---

## Production Deployment Guide

### Deploying to Render / Railway (PaaS)
1. Commit the repository to GitHub.
2. In Render/Railway, create a new **Web Service**.
3. Select the repository and set:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (requires adding `gunicorn` to dependencies)
4. Add the required Environment Variables in the service settings page matching `.env.example`.
5. Since SQLite is serverless, use a persistent disk mount for the database if deploying to Render, or configure a Postgres database backend.

### Deploying to AWS (Elastic Beanstalk / EC2)
1. Launch an EC2 instance (Ubuntu LTS).
2. Install Python, git, and Nginx.
3. Configure a Gunicorn service to run the Flask app.
4. Bind Nginx as a reverse proxy forwarding requests from port 80 to port 5000.
