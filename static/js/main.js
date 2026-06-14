// AgriGuard AI - Core Javascript

// 1. Multi-Language Translations Dictionary
const translations = {
    en: {
        app_name: "AgriGuard AI",
        home: "Home",
        detect_link: "Disease Detection",
        about_link: "About",
        features_link: "Features",
        contact_link: "Contact",
        login_link: "Login",
        register_link: "Register",
        dashboard_link: "Dashboard",
        admin_link: "Admin Panel",
        logout_link: "Logout",
        
        // Hero Section
        hero_title: "AI-Powered Crop Disease Detection",
        hero_subtitle: "Protect your crops and maximize yield using advanced Artificial Intelligence. Scan leaves to diagnose plant diseases instantly.",
        upload_btn: "Start Scan",
        learn_more: "Learn More",
        
        // Benefits
        benefits_title: "Why Choose AgriGuard AI?",
        benefit_1_title: "Instant Results",
        benefit_1_desc: "Get diagnostic reports in seconds with precise actionable treatment recommendations.",
        benefit_2_title: "Highly Accurate",
        benefit_2_desc: "Trained on thousands of crop leaf images, achieving over 96% accuracy rates.",
        benefit_3_title: "Actionable Advice",
        benefit_3_desc: "Receive immediate organic and chemical solutions, fertilizer advice, and pest alerts.",
        
        // Stats
        accuracy_label: "AI Diagnostic Accuracy",
        scans_label: "Total Successful Scans",
        active_farmers: "Active Farmers Registered",
        crops_supported: "Supported Crops",
        
        // Disease Detection Page
        detect_title: "Scan Your Crop Leaf",
        detect_subtitle: "Upload a clear photo of the infected crop leaf to identify the disease using AI.",
        drag_drop: "Drag & Drop leaf image here",
        or_click: "or click to browse files",
        supported_formats: "Supports: JPG, JPEG, PNG (Max 10MB)",
        select_crop: "Crop Type (Optional):",
        crop_auto: "Auto-Detect Crop",
        crop_tomato: "Tomato",
        crop_potato: "Potato",
        crop_corn: "Corn (Maize)",
        crop_rice: "Rice (Paddy)",
        btn_detect: "Detect Crop Disease",
        diagnosing: "Analyzing image with AgriGuard AI...",
        
        // Results
        results_title: "Diagnostic Report",
        confidence: "Confidence Level",
        desc_label: "Disease Description",
        symptoms_label: "Key Symptoms",
        causes_label: "Primary Causes",
        treatment_label: "Treatment Suggestions",
        prevention_label: "Prevention Methods",
        fertilizer_label: "Recommended Fertilizer / Nutrition",
        pesticide_label: "Recommended Pesticide / Chemical Control",
        btn_download_pdf: "Download PDF Report",
        btn_scan_again: "Scan Another Leaf",
        
        // Dashboard
        welcome: "Welcome back,",
        total_scans: "Your Total Scans",
        healthy_pct: "Healthy Crop Ratio",
        detected_diseases: "Diseases Detected",
        recent_activity: "Recent Scan History",
        care_tips: "Daily Crop Care Tips",
        weather_title: "Local Farming Weather",
        weather_hint: "Enable location for real-time agricultural recommendations.",
        no_history: "No scans found. Start by scanning your first crop leaf!",
        
        // Footer
        footer_desc: "AgriGuard AI is dedicated to helping farmers secure crops, reduce chemical inputs, and optimize sustainable harvests through technology.",
        quick_links: "Quick Links",
        copyright: "All Rights Reserved.",
        
        // Contact
        contact_title: "Get in Touch",
        contact_subtitle: "Have questions? Our support team and agronomy experts are here to help you.",
        name_placeholder: "Full Name",
        email_placeholder: "Email Address",
        subject_placeholder: "Subject",
        message_placeholder: "Type your message here...",
        btn_send: "Send Message",
        contact_info: "Contact Information",
        office_loc: "AgriGuard Tech Park, Sector 5, Agri-City",
        office_phone: "+91 98765 43210",
        office_email: "support@agriguard.com"
    },
    hi: {
        app_name: "एग्रीगार्ड एआई",
        home: "होम",
        detect_link: "रोग की पहचान",
        about_link: "हमारे बारे में",
        features_link: "विशेषताएं",
        contact_link: "संपर्क",
        login_link: "लॉगिन",
        register_link: "पंजीकरण",
        dashboard_link: "डैशबोर्ड",
        admin_link: "एडमिन पैनल",
        logout_link: "लॉगआउट",
        
        // Hero Section
        hero_title: "एआई-संचालित फसल रोग पहचान",
        hero_subtitle: "उन्नत कृत्रिम बुद्धिमत्ता (एआई) का उपयोग करके अपनी फसलों की रक्षा करें और उपज बढ़ाएं। पौधों के रोगों का तुरंत निदान करें।",
        upload_btn: "स्कैन शुरू करें",
        learn_more: "और जानें",
        
        // Benefits
        benefits_title: "एग्रीगार्ड एआई क्यों चुनें?",
        benefit_1_title: "तुरंत परिणाम",
        benefit_1_desc: "सटीक और व्यावहारिक उपचार सिफारिशों के साथ कुछ ही सेकंड में निदान रिपोर्ट प्राप्त करें।",
        benefit_2_title: "अत्यंत सटीक",
        benefit_2_desc: "हजारों पत्तियों की छवियों पर प्रशिक्षित, 96% से अधिक सटीकता दर प्राप्त करता है।",
        benefit_3_title: "उपयोगी सलाह",
        benefit_3_desc: "तत्काल जैविक और रासायनिक समाधान, उर्वरक सलाह और कीट अलर्ट प्राप्त करें।",
        
        // Stats
        accuracy_label: "एआई निदान सटीकता",
        scans_label: "कुल सफल स्कैन",
        active_farmers: "सक्रिय किसान पंजीकृत",
        crops_supported: "समर्थित फसलें",
        
        // Disease Detection Page
        detect_title: "अपनी फसल की पत्ती को स्कैन करें",
        detect_subtitle: "एआई का उपयोग करके बीमारी की पहचान करने के लिए संक्रमित फसल की पत्ती की एक स्पष्ट तस्वीर अपलोड करें।",
        drag_drop: "पत्ती की छवि को यहाँ खींचें और छोड़ें",
        or_click: "या फाइलें चुनने के लिए क्लिक करें",
        supported_formats: "समर्थित प्रारूप: JPG, JPEG, PNG (अधिकतम 10MB)",
        select_crop: "फसल का प्रकार (वैकल्पिक):",
        crop_auto: "स्वचालित रूप से फसल पहचानें",
        crop_tomato: "टमाटर",
        crop_potato: "आलू",
        crop_corn: "मक्का",
        crop_rice: "धान (चावल)",
        btn_detect: "फसल रोग की पहचान करें",
        diagnosing: "एग्रीगार्ड एआई छवि का विश्लेषण कर रहा है...",
        
        // Results
        results_title: "निदान रिपोर्ट",
        confidence: "विश्वास स्तर",
        desc_label: "रोग का विवरण",
        symptoms_label: "मुख्य लक्षण",
        causes_label: "प्राथमिक कारण",
        treatment_label: "उपचार के सुझाव",
        prevention_label: "रोकथाम के तरीके",
        fertilizer_label: "अनुशंसित उर्वरक / पोषण",
        pesticide_label: "अनुशंसित कीटनाशक / रासायनिक नियंत्रण",
        btn_download_pdf: "पीडीएफ रिपोर्ट डाउनलोड करें",
        btn_scan_again: "दूसरा पत्ता स्कैन करें",
        
        // Dashboard
        welcome: "स्वागत है,",
        total_scans: "आपके कुल स्कैन",
        healthy_pct: "स्वस्थ फसल अनुपात",
        detected_diseases: "बीमारियों की पहचान हुई",
        recent_activity: "हाल ही का स्कैन इतिहास",
        care_tips: "दैनिक फसल देखभाल युक्तियाँ",
        weather_title: "स्थानीय खेती का मौसम",
        weather_hint: "वास्तविक समय कृषि सिफारिशों के लिए स्थान चालू करें।",
        no_history: "कोई स्कैन नहीं मिला। अपना पहला पत्ता स्कैन करके शुरुआत करें!",
        
        // Footer
        footer_desc: "एग्रीगार्ड एआई प्रौद्योगिकी के माध्यम से फसलों को सुरक्षित रखने, रासायनिक उपयोग को कम करने और टिकाऊ कटाई को बढ़ावा देने के लिए समर्पित है।",
        quick_links: "त्वरित लिंक",
        copyright: "सर्वाधिकार सुरक्षित।",
        
        // Contact
        contact_title: "संपर्क करें",
        contact_subtitle: "कोई सवाल है? हमारी सहायता टीम और कृषि विशेषज्ञ आपकी मदद के लिए तैयार हैं।",
        name_placeholder: "पूरा नाम",
        email_placeholder: "ईमेल पता",
        subject_placeholder: "विषय",
        message_placeholder: "अपना संदेश यहाँ लिखें...",
        btn_send: "संदेश भेजें",
        contact_info: "संपर्क जानकारी",
        office_loc: "एग्रीगार्ड टेक पार्क, सेक्टर 5, कृषि-नगर",
        office_phone: "+91 98765 43210",
        office_email: "support@agriguard.com"
    },
    ta: {
        app_name: "அக்ரிகார்ட் AI",
        home: "முகப்பு",
        detect_link: "நோய் கண்டறிதல்",
        about_link: "எங்களைப் பற்றி",
        features_link: "அம்சங்கள்",
        contact_link: "தொடர்பு",
        login_link: "உள்நுழை",
        register_link: "பதிவு செய்க",
        dashboard_link: "டாஷ்போர்டு",
        admin_link: "நிர்வாகக் குழு",
        logout_link: "வெளியேறு",
        
        // Hero Section
        hero_title: "AI-ஆல் இயங்கும் பயிர் நோய் கண்டறிதல்",
        hero_subtitle: "செயற்கை நுண்ணறிவு தொழில்நுட்பத்தைப் பயன்படுத்தி உங்கள் பயிர்களைப் பாதுகாத்து மகசூலை அதிகரிக்கவும். இலைகளை ஸ்கேன் செய்து உடனடியாக நோயைக் கண்டறியவும்.",
        upload_btn: "ஸ்கேன் செய்க",
        learn_more: "மேலும் அறிய",
        
        // Benefits
        benefits_title: "ஏன் அக்ரிகார்ட் AI-ஐ தேர்வு செய்ய வேண்டும்?",
        benefit_1_title: "உடனடி முடிவுகள்",
        benefit_1_desc: "துல்லியமான மற்றும் பயனுள்ள சிகிச்சை பரிந்துரைகளுடன் நொடிகளில் நோய் கண்டறிதல் அறிக்கையைப் பெறுங்கள்.",
        benefit_2_title: "மிகவும் துல்லியமானது",
        benefit_2_desc: "ஆயிரக்கணக்கான பயிர் இலை படங்களைக் கொண்டு பயிற்றுவிக்கப்பட்டது, 96% க்கும் அதிகமான துல்லியத்தைப் பெறுகிறது.",
        benefit_3_title: "செயல்பாட்டு ஆலோசனை",
        benefit_3_desc: "உடனடி இயற்கை மற்றும் ரசாயன தீர்வுகள், உர ஆலோசனைகள் மற்றும் பூச்சி எச்சரிக்கைகளைப் பெறுங்கள்.",
        
        // Stats
        accuracy_label: "AI கண்டறிதல் துல்லியம்",
        scans_label: "மொத்த வெற்றிகரமான ஸ்கேன்கள்",
        active_farmers: "பதிவுசெய்த விவசாயிகளின் எண்ணிக்கை",
        crops_supported: "ஆதரிக்கப்படும் பயிர்கள்",
        
        // Disease Detection Page
        detect_title: "உங்கள் பயிர் இலையை ஸ்கேன் செய்யுங்கள்",
        detect_subtitle: "AI மூலம் நோயைக் கண்டறிய பாதிக்கப்பட்ட பயிர் இலையின் தெளிவான படத்தை பதிவேற்றவும்.",
        drag_drop: "இலை படத்தை இங்கே இழுத்து விடவும்",
        or_click: "அல்லது கோப்புகளைத் தேர்ந்தெடுக்க கிளிக் செய்யவும்",
        supported_formats: "ஆதரிக்கப்படும் வடிவங்கள்: JPG, JPEG, PNG (அதிகபட்சம் 10MB)",
        select_crop: "பயிர் வகை (விருப்பத்திற்குரியது):",
        crop_auto: "பயிரை தானாகக் கண்டறி",
        crop_tomato: "தக்காளி",
        crop_potato: "உருளைக்கிழங்கு",
        crop_corn: "சோளம்",
        crop_rice: "நெல் (அரிசி)",
        btn_detect: "பயிர் நோயைக் கண்டறி",
        diagnosing: "அக்ரிகார்ட் AI படத்தை பகுப்பாய்வு செய்கிறது...",
        
        // Results
        results_title: "நோய் கண்டறிதல் அறிக்கை",
        confidence: "நம்பகத்தன்மை அளவு",
        desc_label: "நோய் விளக்கம்",
        symptoms_label: "முக்கிய அறிகுறிகள்",
        causes_label: "முதன்மைக் காரணங்கள்",
        treatment_label: "சிகிச்சை பரிந்துரைகள்",
        prevention_label: "தடுப்பு முறைகள்",
        fertilizer_label: "பரிந்துரைக்கப்பட்ட உரம் / ஊட்டச்சத்து",
        pesticide_label: "பரிந்துரைக்கப்பட்ட பூச்சிக்கொல்லி / இரசாயன கட்டுப்பாடு",
        btn_download_pdf: "அறிக்கையை PDF ஆக பதிவிறக்கு",
        btn_scan_again: "மற்றொரு இலையை ஸ்கேன் செய்",
        
        // Dashboard
        welcome: "மீண்டும் வருக,",
        total_scans: "உங்களது மொத்த ஸ்கேன்கள்",
        healthy_pct: "ஆரோக்கியமான பயிர் விகிதம்",
        detected_diseases: "கண்டறியப்பட்ட நோய்கள்",
        recent_activity: "சமீபத்திய ஸ்கேன் வரலாறு",
        care_tips: "தினசரி பயிர் பராமரிப்பு குறிப்புகள்",
        weather_title: "உள்ளூர் விவசாய வானிலை",
        weather_hint: "உண்மையான நேர வானிலை அடிப்படையிலான பயிர் ஆலோசனைகளுக்கு இருப்பிடத்தை அனுமதிக்கவும்.",
        no_history: "ஸ்கேன்கள் எதுவும் இல்லை. உங்கள் முதல் பயிர் இலையை ஸ்கேன் செய்யத் தொடங்குங்கள்!",
        
        // Footer
        footer_desc: "தொழில்நுட்பத்தின் மூலம் பயிர்களைப் பாதுகாக்கவும், ரசாயன பயன்பாட்டைக் குறைக்கவும், நிலையான விளைச்சலை அதிகரிக்கவும் அக்ரிகார்ட் AI அர்ப்பணிக்கப்பட்டுள்ளது.",
        quick_links: "விரைவு இணைப்புகள்",
        copyright: "அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை.",
        
        // Contact
        contact_title: "தொடர்பு கொள்ள",
        contact_subtitle: "கேள்விகள் உள்ளதா? எங்களது ஆதரவுக் குழுவும் பயிர் நிபுணர்களும் உங்களுக்கு உதவக் காத்திருக்கிறார்கள்.",
        name_placeholder: "முழு பெயர்",
        email_placeholder: "மின்னஞ்சல் முகவரி",
        subject_placeholder: "தலைப்பு",
        message_placeholder: "உங்கள் செய்தியை இங்கே தட்டச்சு செய்க...",
        btn_send: "செய்தி அனுப்பு",
        contact_info: "தொடர்புத் தகவல்கள்",
        office_loc: "அக்ரிகார்ட் டெக் பார்க், செக்டர் 5, அக்ரி-சிட்டி",
        office_phone: "+91 98765 43210",
        office_email: "support@agriguard.com"
    }
};

// 2. Language Engine Execution
function setLanguage(lang) {
    localStorage.setItem('lang', lang);
    const trans = translations[lang] || translations.en;
    
    // Update simple translation attributes
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (trans[key]) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = trans[key];
            } else {
                element.textContent = trans[key];
            }
        }
    });

    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Update active state in language dropdown
    const langBtn = document.getElementById('langDropdownBtn');
    if (langBtn) {
        const langMap = { en: 'English', hi: 'हिन्दी', ta: 'தமிழ்' };
        langBtn.textContent = langMap[lang] || 'English';
    }
}

// 3. Dark Mode Core Logic
function initTheme() {
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
        const themeIcon = themeBtn.querySelector('i');
        if (currentTheme === 'dark') {
            themeIcon.className = 'bi bi-sun-fill';
        } else {
            themeIcon.className = 'bi bi-moon-fill';
        }
    }
}

function toggleTheme() {
    const activeTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
        const themeIcon = themeBtn.querySelector('i');
        if (newTheme === 'dark') {
            themeIcon.className = 'bi bi-sun-fill';
        } else {
            themeIcon.className = 'bi bi-moon-fill';
        }
    }
}

// 4. Geolocation and Weather Integration (Open-Meteo)
function initWeather() {
    const weatherSection = document.getElementById('weather-widget-content');
    if (!weatherSection) return; // Exit if weather card isn't on the page

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                fetchWeather(position.coords.latitude, position.coords.longitude);
            },
            (error) => {
                console.log("Geolocation access denied or failed. Loading default coordinates (Chennai/India).");
                fetchWeather(13.0827, 80.2707); // Fallback to Chennai coordinates
            }
        );
    } else {
        fetchWeather(13.0827, 80.2707);
    }
}

async function fetchWeather(lat, lon) {
    const tempElement = document.getElementById('weather-temp');
    const descElement = document.getElementById('weather-desc');
    const windElement = document.getElementById('weather-wind');
    const humidityElement = document.getElementById('weather-humidity');
    const adviceElement = document.getElementById('weather-advice');
    
    try {
        const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&hourly=relativehumidity_2m`);
        if (!response.ok) throw new Error("Weather request failed");
        
        const data = await response.json();
        const cur = data.current_weather;
        
        // Convert weather codes to reader friendly descriptors
        const codeMap = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Foggy", 48: "Depositing rime fog",
            51: "Drizzle: Light", 53: "Drizzle: Moderate", 55: "Drizzle: Dense",
            61: "Rain: Slight", 63: "Rain: Moderate", 65: "Rain: Heavy intensity",
            71: "Snow fall: Slight", 73: "Snow fall: Moderate", 75: "Snow fall: Heavy",
            80: "Rain showers: Slight", 81: "Rain showers: Moderate", 82: "Rain showers: Violent",
            95: "Thunderstorm: Slight or moderate", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
        };
        
        const weatherDesc = codeMap[cur.weathercode] || "Mild conditions";
        const temp = Math.round(cur.temperature);
        const wind = cur.windspeed;
        
        // Try to fetch current hour humidity from hourly array
        let humidity = 65; // Default fallback
        if (data.hourly && data.hourly.relativehumidity_2m) {
            humidity = data.hourly.relativehumidity_2m[0];
        }

        // Render UI
        if (tempElement) tempElement.textContent = `${temp}°C`;
        if (descElement) descElement.textContent = weatherDesc;
        if (windElement) windElement.textContent = `Wind: ${wind} km/h`;
        if (humidityElement) humidityElement.textContent = `Humidity: ${humidity}%`;
        
        // Generate farming recommendations based on weather
        let advisory = "Conditions are normal. Perfect for general field maintenance and weeding.";
        if (cur.weathercode >= 51 && cur.weathercode <= 82) {
            advisory = "Rain is forecast. Avoid spraying foliar pesticides or fertilizers as they may wash off. Keep drainage canals clear.";
        } else if (temp > 35) {
            advisory = "High heat alert. Increase soil irrigation in the early morning or evening. Mulch crops to prevent water evaporation.";
        } else if (humidity > 80 && temp < 25) {
            advisory = "Cool and humid conditions. High risk of late blight fungal infection. Monitor leaves closely for spots and apply protectant sprays.";
        }
        if (adviceElement) adviceElement.textContent = advisory;

    } catch (error) {
        console.error("Failed to load live weather. Using simulated offline agricultural weather data.", error);
        // Offline fallback
        if (tempElement) tempElement.textContent = "28°C";
        if (descElement) descElement.textContent = "Partly Cloudy";
        if (windElement) windElement.textContent = "Wind: 12 km/h";
        if (humidityElement) humidityElement.textContent = "Humidity: 60%";
        if (adviceElement) adviceElement.textContent = "Optimal conditions for agricultural spray applications and organic fertilizing.";
    }
}

// 5. Drag and Drop Uploader Script (Detect page specific)
function initUploader() {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('image-input');
    const preview = document.getElementById('preview-image');
    const uploaderPrompt = document.getElementById('uploader-prompt');
    const btnDetect = document.getElementById('btn-detect');
    const cropSelect = document.getElementById('crop_type');
    const loadingOverlay = document.getElementById('loading-overlay');
    const resultsContainer = document.getElementById('results-container');

    if (!dropzone || !fileInput) return; // Exit if not on the detection page

    // Trigger click on file input
    dropzone.addEventListener('click', () => fileInput.click());

    // Highlight drop area when files dragged over
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dragover');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dragover');
        }, false);
    });

    // Handle dropped files
    dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length) {
            fileInput.files = files;
            handleFileSelect(files[0]);
        }
    });

    // Handle selected files
    fileInput.addEventListener('change', (e) => {
        if (fileInput.files.length) {
            handleFileSelect(fileInput.files[0]);
        }
    });

    function handleFileSelect(file) {
        // Validate type
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
        if (!validTypes.includes(file.type)) {
            alert("Please upload a valid image file (JPG, JPEG, or PNG).");
            return;
        }

        // Validate size (10 MB limit)
        if (file.size > 10 * 1024 * 1024) {
            alert("File size exceeds 10 MB limit.");
            return;
        }

        // Generate visual preview
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            preview.src = reader.result;
            preview.style.display = 'block';
            uploaderPrompt.style.display = 'none';
            btnDetect.removeAttribute('disabled');
        }
    }

    // Async Request Form submit handler
    const uploadForm = document.getElementById('upload-form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const file = fileInput.files[0];
            if (!file) return;

            // Show loading
            loadingOverlay.style.display = 'flex';
            btnDetect.setAttribute('disabled', 'true');
            if (resultsContainer) resultsContainer.style.display = 'none';

            const formData = new FormData();
            formData.append('image', file);
            formData.append('crop_type', cropSelect.value);

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();
                loadingOverlay.style.display = 'none';
                btnDetect.removeAttribute('disabled');

                if (data.status === 'success') {
                    displayPredictionResults(data);
                } else {
                    alert("Prediction Error: " + data.message);
                }
            } catch (err) {
                loadingOverlay.style.display = 'none';
                btnDetect.removeAttribute('disabled');
                console.error(err);
                alert("Failed to reach server. Please check your internet connection.");
            }
        });
    }

    function displayPredictionResults(data) {
        if (!resultsContainer) return;
        
        // Populating dynamic fields
        document.getElementById('res-disease').textContent = data.disease_name;
        document.getElementById('res-confidence').textContent = `${data.confidence.toFixed(2)}%`;
        document.getElementById('res-desc').textContent = data.details.description;
        
        // Populate symptoms bullet list
        const symList = document.getElementById('res-symptoms');
        symList.innerHTML = '';
        data.details.symptoms.split('. ').forEach(sym => {
            if (sym.trim()) {
                const li = document.createElement('li');
                li.className = 'mb-1';
                li.textContent = sym.trim();
                symList.appendChild(li);
            }
        });

        // Populate causes
        document.getElementById('res-causes').textContent = data.details.causes;

        // Populate treatment list
        const treatList = document.getElementById('res-treatment');
        treatList.innerHTML = '';
        data.details.treatment.split('. ').forEach(t => {
            if (t.trim()) {
                const li = document.createElement('li');
                li.className = 'mb-1';
                li.textContent = t.trim();
                treatList.appendChild(li);
            }
        });

        // Populate prevention list
        const prevList = document.getElementById('res-prevention');
        prevList.innerHTML = '';
        data.details.prevention.split('. ').forEach(p => {
            if (p.trim()) {
                const li = document.createElement('li');
                li.className = 'mb-1';
                li.textContent = p.trim();
                prevList.appendChild(li);
            }
        });

        // Recommendations
        document.getElementById('res-fertilizer').textContent = data.details.fertilizers;
        document.getElementById('res-pesticide').textContent = data.details.pesticides;

        // PDF download button URI
        const pdfBtn = document.getElementById('res-pdf-link');
        if (pdfBtn) {
            pdfBtn.href = `/download_report/${data.prediction_id}`;
        }

        // Show Results container
        resultsContainer.style.display = 'block';
        
        // Smooth scroll to results
        resultsContainer.scrollIntoView({ behavior: 'smooth' });

        // Draw Confidence Chart using Chart.js
        drawConfidenceChart(data.confidence);
    }

    let confidenceChart = null;
    function drawConfidenceChart(confidence) {
        const ctx = document.getElementById('confidenceChartCanvas').getContext('2d');
        
        // Destroy existing chart to prevent canvas redraw bugs
        if (confidenceChart) {
            confidenceChart.destroy();
        }

        const primaryColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim() || '#2E7D32';
        const borderColor = getComputedStyle(document.documentElement).getPropertyValue('--border-color').trim() || '#E0E4E0';
        
        confidenceChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [confidence, 100 - confidence],
                    backgroundColor: [primaryColor, borderColor],
                    borderWidth: 0
                }]
            },
            options: {
                cutout: '80%',
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { display: false },
                    tooltip: { enabled: false }
                }
            }
        });
    }
}

// 6. Global DOM Listeners & Actions initialization
document.addEventListener('DOMContentLoaded', () => {
    // Check local storage for language
    const userLang = localStorage.getItem('lang') || 'en';
    setLanguage(userLang);

    // Bind language events
    document.querySelectorAll('.lang-select-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = item.getAttribute('data-lang');
            setLanguage(lang);
        });
    });

    // Theme setup
    initTheme();
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
        themeBtn.addEventListener('click', toggleTheme);
    }

    // Initialize dropzone uploader
    initUploader();

    // Initialize local weather panel
    initWeather();
    
    // Smooth navigation active indicator updater
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
