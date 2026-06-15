import os
import psycopg
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
from psycopg import sql

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    """Connect to Supabase PostgreSQL database"""
    conn = psycopg.connect(DATABASE_URL)
    return conn

def init_db():
    """Initialize database tables and insert seed data"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'farmer',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Predictions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users (id) ON DELETE CASCADE,
        image_path TEXT NOT NULL,
        disease_name TEXT NOT NULL,
        confidence REAL NOT NULL,
        prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Diseases Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diseases (
        id SERIAL PRIMARY KEY,
        disease_name TEXT UNIQUE NOT NULL,
        crop TEXT NOT NULL,
        description TEXT NOT NULL,
        symptoms TEXT NOT NULL,
        causes TEXT NOT NULL,
        treatment TEXT NOT NULL,
        prevention TEXT NOT NULL,
        fertilizers TEXT NOT NULL,
        pesticides TEXT NOT NULL
    )
    ''')

    # Create Contacts Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Prediction Logs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prediction_logs (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users (id) ON DELETE CASCADE,
        ip_address TEXT,
        disease_name TEXT NOT NULL,
        confidence REAL NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()

    # Insert Disease Data
    diseases_data = [
        # TOMATO
        (
            "Tomato Early Blight",
            "Tomato",
            "Early blight is a common tomato disease caused by the fungus Alternaria solani. It affects leaves, stems, and fruit, causing significant yield loss if left unchecked.",
            "Dark spots with concentric rings (resembling a target) form on older leaves first. Surrounding leaf tissue turns yellow, and leaves eventually die and drop off. Dark, sunken spots may also develop at the stem end of fruits.",
            "The fungus Alternaria solani overwinter in crop debris and soil. Spores are spread by wind, rain, splashing water, and insects. Warm, humid, or rainy weather promotes disease development.",
            "Apply copper-based fungicides or protectant fungicides at regular intervals. Prune the lower branches of the plants to improve air circulation and prevent soil contact.",
            "Rotate tomato crops with non-solanaceous crops (e.g., legumes or corn) every 3 years. Use drip irrigation instead of overhead watering to keep foliage dry. Mulch the soil around plants to prevent spores from splashing onto leaves.",
            "Use fertilizers containing calcium (like calcium nitrate) to support cell wall strength, and avoid excess nitrogen which creates lush foliage susceptible to disease.",
            "Chlorothalonil, copper-based fungicides, or Mancozeb."
        ),
        (
            "Tomato Late Blight",
            "Tomato",
            "Late blight is a highly destructive disease caused by the water mold Phytophthora infestans. It can rapidly destroy entire tomato fields in cool, wet conditions.",
            "Large, irregular water-soaked spots appear on leaves, turning brown and papery. In humid weather, a white, fuzzy growth forms on the underside of leaves. Dark brown, firm lesions appear on the fruit.",
            "The pathogen Phytophthora infestans is carried by wind currents and thrives in cool (15-20°C), wet, and humid environments.",
            "Destroy all infected plant parts immediately. Apply systemic fungicides such as mefenoxam or copper fungicides if caught early.",
            "Plant resistant tomato varieties. Avoid planting tomatoes near potatoes. Ensure proper spacing for ventilation and water early in the day so leaves dry quickly.",
            "Apply balanced fertilizer with high potassium to boost disease resistance, avoiding excess nitrogen.",
            "Mefenoxam, Copper Fungicide, Azoxystrobin."
        ),
        (
            "Tomato Healthy",
            "Tomato",
            "The tomato crop is healthy, shows robust growth, vibrant green leaves, and has no visible signs of infection or pests.",
            "Foliage is vibrant green, firm, and free of spots or discoloration. Stems are strong and erect, and fruits are developing naturally without dark lesions.",
            "Optimal watering, proper spacing, healthy soil, and preventative care.",
            "No active treatment required. Continue standard cultural practices.",
            "Maintain regular crop monitoring. Keep up weed control and ensure consistent, moderate soil moisture.",
            "Apply balanced NPK fertilizer (e.g., 10-10-10) or organic compost to support ongoing fruit production.",
            "None required. Can use organic neem oil periodically as a preventative pest repellant."
        ),
        # POTATO
        (
            "Potato Early Blight",
            "Potato",
            "Potato early blight, caused by Alternaria solani, is a foliar disease that reduces tuber size and yield. It mostly targets older, stressed foliage.",
            "Small, dark, circular spots with concentric rings appear on older leaves. The spots can expand and join, causing leaves to curl and dry up.",
            "Fungus spores overwinter in potato debris or soil. Spreads via wind and rain splash in alternating wet and dry conditions.",
            "Apply foliar fungicides. Remove and burn infected plant debris after harvest.",
            "Use certified disease-free seed potatoes. Plant in well-drained soils. Avoid overhead irrigation and practice a 3-year crop rotation.",
            "Maintain optimal soil fertility with balanced NPK and trace minerals to prevent plant stress.",
            "Chlorothalonil, Mancozeb, or copper fungicides."
        ),
        (
            "Potato Late Blight",
            "Potato",
            "Potato late blight, caused by Phytophthora infestans, is famous for causing the Irish Potato Famine. It can destroy crops within days.",
            "Pale green, water-soaked spots appear at leaf tips or margins, turning dark brown/black. White mold grows on leaf undersides in wet conditions. Infected tubers show a brown, dry rot.",
            "Pathogen spreads via infected seed tubers, cull piles, and wind-blown spores during cool, damp weather.",
            "Harvest crops during dry weather. Spray protectant and systemic fungicides. Destroy infected vines before harvest.",
            "Plant resistant varieties. Kill volunteer potato plants. Do not harvest when vines are wet.",
            "Apply high-potassium and calcium fertilizers to strengthen potato cell walls.",
            "Metalaxyl, Mancozeb, Copper sulfate."
        ),
        (
            "Potato Healthy",
            "Potato",
            "The potato crop is healthy, exhibiting strong green foliage and healthy root/tuber systems.",
            "Vigorous green leaves, strong upright stems, and absence of lesions, spots, or white mold.",
            "Optimal temperature, proper hilling, consistent watering, and balanced nutrients.",
            "No active treatment required.",
            "Keep potato plants hilled to protect tubers. Rotate crops and monitor fields weekly.",
            "Use balanced NPK fertilizer. Apply gypsum (calcium sulfate) for skin quality and tuber health.",
            "None required. Keep watch for potato beetles and treat organically if needed."
        ),
        # CORN
        (
            "Corn Rust",
            "Corn",
            "Common rust is a fungal disease caused by Puccinia sorghi. It is easily recognizable and occurs globally, reducing grain yield in severe cases.",
            "Golden-brown to reddish-orange powdery pustules (spots) appear on both upper and lower leaf surfaces. In late season, these pustules turn black.",
            "Spores of Puccinia sorghi are carried long distances by wind. The fungus requires free moisture on leaves and cool temperatures (15-22°C) to infect.",
            "Apply foliar fungicides at the first sign of rust pustules, especially if weather remains cool and damp.",
            "Plant resistant corn hybrids. Manage weeds to improve air circulation within the field canopy.",
            "Ensure adequate nitrogen and potassium fertilization to support plant vigor and recovery.",
            "Pyraclostrobin, Tebuconazole, Propiconazole."
        ),
        (
            "Corn Leaf Spot",
            "Corn",
            "Gray leaf spot is a highly damaging fungal disease of corn caused by Cercospora zeae-maydis. It can cause severe defoliation and stalk lodging.",
            "Small, tan or gray, rectangular spots with dark borders run parallel to leaf veins. As the disease progresses, entire leaves turn brown and die.",
            "The fungus overwinters in corn residue left on the soil surface. Spores are splashed by rain or wind onto new corn leaves during warm, humid weather.",
            "Apply triazole or strobilurin-based fungicides early in the season when lesions are first spotted on lower leaves.",
            "Rotate corn with non-grass crops. Perform tillage to bury infected corn residue. Use resistant hybrids.",
            "Apply balanced fertilizer with proper potassium levels to reduce disease severity.",
            "Azoxystrobin, Propiconazole, Pyraclostrobin."
        ),
        (
            "Corn Healthy",
            "Corn",
            "The corn crop is in excellent condition, showing thick green leaves, sturdy stalks, and healthy ear development.",
            "Vibrant green leaves, uniform growth, no rust pustules or rectangular lesions, and clean, strong stalks.",
            "Good soil drainage, optimal nitrogen fertilization, and clean tillage/rotation.",
            "No treatment needed.",
            "Maintain proper plant population density for ventilation, keep up with weed management.",
            "Apply nitrogen side-dressing during early vegetative growth stages (V4-V6) and ensure good phosphorus/potassium levels.",
            "None required."
        ),
        # RICE
        (
            "Rice Blast",
            "Rice",
            "Rice blast, caused by the fungus Magnaporthe oryzae, is one of the most destructive diseases of rice, affecting leaves, nodes, panicles, and grains.",
            "Spindle-shaped (diamond-shaped) spots with reddish-brown borders and gray/white centers appear on leaves. Node infections cause stems to break (node blast), and panicle infections cause empty grains (neck blast).",
            "The fungus spreads via wind-borne spores. Thrives in cool temperatures, high relative humidity, and when leaves remain wet for long periods.",
            "Apply systemic fungicides (e.g., tricyclazole) during the early leaf blast phase or at heading stage to prevent neck blast.",
            "Plant blast-resistant rice cultivars. Avoid over-application of nitrogen fertilizer. Keep field water levels consistent.",
            "Apply silicon-based fertilizers to strengthen leaf epidermal cells, making them harder for fungal spores to penetrate.",
            "Tricyclazole, Carbendazim, Kasugamycin."
        ),
        (
            "Rice Brown Spot",
            "Rice",
            "Brown spot is a fungal disease caused by Bipolaris oryzae. It is often associated with poorly drained, nutrient-deficient, or dry soils.",
            "Numerous small, oval, dark brown spots (resembling sesame seeds) with yellow halos appear on leaf blades. Heavy infections cover entire leaves, causing them to dry up.",
            "The fungus Bipolaris oryzae is seed-borne and survives in crop residues. Thrives in high humidity and dry or nutrient-starved soils.",
            "Spray copper or systemic fungicides. Seed treatment before sowing is highly effective.",
            "Provide balanced crop nutrition, especially potassium, silica, and calcium. Use clean seed. Improve soil drainage and organic matter.",
            "Apply muriate of potash (MOP) and silicon fertilizers to correct nutrient deficiency.",
            "Mancozeb, Propiconazole, Edifenphos."
        ),
        (
            "Rice Healthy",
            "Rice",
            "The rice crop is healthy, showing upright green leaves, strong tillering, and uniform panicle initiation.",
            "Bright, clean green leaf blades without brown spots or spindle lesions. Dense tillers and healthy root system.",
            "Correct water level management, balanced fertilization (nitrogen-silicon balance), and clean seed use.",
            "No active treatment required.",
            "Ensure regular wet-and-dry irrigation cycles. Keep dikes clean of weeds.",
            "Use split applications of nitrogen fertilizer, and ensure adequate potassium and zinc levels in the soil.",
            "None required. Periodic organic bio-pesticide spray (neem-based) can prevent stem borers."
        )
    ]

    for d in diseases_data:
        try:
            cursor.execute('''
            INSERT INTO diseases (
                disease_name, crop, description, symptoms, causes, treatment, prevention, fertilizers, pesticides
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (disease_name) DO NOTHING
            ''', d)
        except Exception as e:
            print(f"Error inserting disease: {e}")
            pass

    conn.commit()

    # Create Default Admin User
    admin_email = os.getenv('ADMIN_EMAIL', 'admin@agriguard.com')
    admin_password = os.getenv('ADMIN_PASSWORD', 'adminpassword123')
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (admin_email,))
    admin_exists = cursor.fetchone()
    
    if not admin_exists:
        hashed_password = generate_password_hash(admin_password)
        cursor.execute('''
        INSERT INTO users (name, email, phone, password, role)
        VALUES (%s, %s, %s, %s, %s)
        ''', ('Administrator', admin_email, '0000000000', hashed_password, 'admin'))
        conn.commit()
        print(f"Default admin account created: {admin_email}")

    conn.close()
    print("Supabase database initialized successfully.")

if __name__ == "__main__":
    init_db()
