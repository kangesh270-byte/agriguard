import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_report_pdf(prediction, disease_details, user_name, user_email):
    """
    Generates a professional PDF report for a given prediction scan.
    Returns: BytesIO object containing the PDF data.
    """
    buffer = io.BytesIO()
    
    # Page setup
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Define custom colors
    primary_color = colors.HexColor("#2E7D32")    # Dark Green
    secondary_color = colors.HexColor("#81C784")  # Light Green
    dark_neutral = colors.HexColor("#212121")     # Charcoal
    light_bg = colors.HexColor("#F5F5F5")         # Warm White
    accent_red = colors.HexColor("#C62828")       # Red (low confidence, etc.)
    
    # Custom Paragraph Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        alignment=0, # Left-aligned
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#757575"),
        spaceAfter=15
    )
    
    h2_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=dark_neutral,
        spaceAfter=8
    )
    
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    callout_title_style = ParagraphStyle(
        'CalloutTitle',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=primary_color,
        spaceAfter=2
    )

    story = []
    
    # 1. Header (Logo / Title Block)
    story.append(Paragraph("AgriGuard AI – Crop Care Report", title_style))
    date_str = datetime.now().strftime("%B %d, %Y - %I:%M %p")
    story.append(Paragraph(f"Empowering Farmers with Deep Learning Disease Detection | Generated on {date_str}", subtitle_style))
    
    # Decorative colored bar
    bar_table = Table([['']], colWidths=[532], rowHeights=[4])
    bar_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), primary_color),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(bar_table)
    story.append(Spacer(1, 15))
    
    # 2. Metadata Section (Farmer info & scan info)
    meta_data = [
        [
            Paragraph("<b>Farmer Details:</b>", body_style),
            Paragraph(f"Name: {user_name}<br/>Email: {user_email}", body_style),
            Paragraph("<b>Scan Information:</b>", body_style),
            Paragraph(f"Crop: {disease_details['crop']}<br/>Scan ID: #{prediction['id']}", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[110, 156, 110, 156])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E0E0E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E0E0E0")),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 15))
    
    # 3. Prediction Result Block
    conf = prediction['confidence']
    conf_color = primary_color if conf > 80 else (secondary_color if conf > 60 else accent_red)
    
    result_data = [
        [
            Paragraph("<b>Detected Disease / Condition</b>", body_style),
            Paragraph("<b>Confidence Level</b>", body_style)
        ],
        [
            Paragraph(f"<font size=16 color='{primary_color.hexval()}'><b>{prediction['disease_name']}</b></font>", body_style),
            Paragraph(f"<font size=16 color='{conf_color.hexval()}'><b>{conf:.2f}%</b></font>", body_style)
        ]
    ]
    result_table = Table(result_data, colWidths=[350, 182])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOX', (0,0), (-1,-1), 1, primary_color),
    ]))
    # Quick fix for text color in header
    result_data[0][0].style.textColor = colors.white
    result_data[0][1].style.textColor = colors.white
    
    story.append(result_table)
    story.append(Spacer(1, 15))
    
    # 4. Disease Detailed Information
    story.append(Paragraph("Disease Description", h2_style))
    story.append(Paragraph(disease_details['description'], body_style))
    
    story.append(Paragraph("Key Symptoms", h2_style))
    symptoms = disease_details['symptoms'].split('. ')
    for sym in symptoms:
        if sym.strip():
            # Add dot if missing
            text = sym.strip() + "." if not sym.strip().endswith('.') else sym.strip()
            story.append(Paragraph(f"• {text}", bullet_style))
            
    story.append(Paragraph("Primary Causes", h2_style))
    story.append(Paragraph(disease_details['causes'], body_style))
    
    story.append(Paragraph("Treatment Suggestions", h2_style))
    treatments = disease_details['treatment'].split('. ')
    for treat in treatments:
        if treat.strip():
            text = treat.strip() + "." if not treat.strip().endswith('.') else treat.strip()
            story.append(Paragraph(f"• {text}", bullet_style))
            
    story.append(Paragraph("Prevention Methods", h2_style))
    preventions = disease_details['prevention'].split('. ')
    for prev in preventions:
        if prev.strip():
            text = prev.strip() + "." if not prev.strip().endswith('.') else prev.strip()
            story.append(Paragraph(f"• {text}", bullet_style))
            
    story.append(Spacer(1, 10))
    
    # 5. Recommended Inputs (Fertilizers & Pesticides)
    recommend_data = [
        [
            Paragraph("<b>Recommended Fertilizer / Nutrition Care</b>", callout_title_style),
            Paragraph("<b>Recommended Pesticides / Chemical Action</b>", callout_title_style)
        ],
        [
            Paragraph(disease_details['fertilizers'], body_style),
            Paragraph(disease_details['pesticides'], body_style)
        ]
    ]
    recommend_table = Table(recommend_data, colWidths=[266, 266])
    recommend_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#E8F5E9")), # Very light green background
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, secondary_color),
        ('LINEBEFORE', (1,0), (1,-1), 0.5, secondary_color),
    ]))
    story.append(recommend_table)
    story.append(Spacer(1, 20))
    
    # Footer Notice
    story.append(Paragraph("<b>Disclaimer:</b> AgriGuard AI disease diagnosis is powered by computer vision algorithms. Results should be cross-referenced with local agricultural experts or extension services. Always read pesticide and fertilizer labels carefully before application.", subtitle_style))
    
    # Build Document
    doc.build(story)
    
    buffer.seek(0)
    return buffer
