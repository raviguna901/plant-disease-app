from flask import Flask, render_template, request, send_file, redirect
import os, sqlite3
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from werkzeug.utils import secure_filename
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# ---------------- INIT ----------------

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MODEL_PATH = "Mobilenetv2.h5"

# ---------------- LOAD MODEL ----------------

model = load_model(MODEL_PATH)
print("✓ Model loaded")

# ---------------- CLASSES ----------------

CLASS_NAMES = [
'Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy',
'Blueberry___healthy','Cherry___Powdery_mildew','Cherry___healthy',
'Corn___Cercospora','Corn___Common_rust','Corn___Northern_Blight','Corn___healthy',
'Grape___Black_rot','Grape___Esca','Grape___Leaf_blight','Grape___healthy',
'Orange___Haunglongbing','Peach___Bacterial_spot','Peach___healthy',
'Pepper___Bacterial_spot','Pepper___healthy','Potato___Early_blight',
'Potato___Late_blight','Potato___healthy','Raspberry___healthy',
'Soybean___healthy','Squash___Powdery_mildew','Strawberry___Leaf_scorch',
'Strawberry___healthy','Tomato___Bacterial_spot','Tomato___Early_blight',
'Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria',
'Tomato___Spider_mites','Tomato___Target_Spot','Tomato___Yellow_Leaf_Curl',
'Tomato___Mosaic','Tomato___healthy'
]

DISEASE_INFO = {
"Apple - Black rot":{
"desc":"Black rot is a fungal disease causing dark lesions on leaves.",
"remedy":"Remove infected leaves and apply fungicide."
}
}

# ---------------- DATABASE ----------------

def save_history(disease,conf):
    con = sqlite3.connect("history.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS history(disease TEXT, confidence REAL)")
    cur.execute("INSERT INTO history VALUES (?,?)",(disease,conf))
    con.commit()
    con.close()

# ---------------- IMAGE PROCESS ----------------

def preprocess(path):
    img = Image.open(path).resize((256,256)).convert("RGB")
    arr = np.array(img)/255.0
    arr = np.expand_dims(arr,0)
    return arr

def predict_disease(path):
    img = preprocess(path)
    preds = model.predict(img,verbose=0)
    idx = np.argmax(preds)
    conf = float(np.max(preds))*100
    disease = CLASS_NAMES[idx].replace("___"," - ").replace("_"," ")
    return disease, round(conf,2)

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    file = request.files["file"]
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    disease, confidence = predict_disease(path)

    info = DISEASE_INFO.get(disease,{
        "desc":"No description available.",
        "remedy":"Consult agriculture expert."
    })

    save_history(disease,confidence)

    return render_template("result.html",
        disease=disease,
        confidence=confidence,
        image=filename,
        description=info["desc"],
        remedy=info["remedy"]
    )

@app.route("/download_report")
def download_report():

    disease = request.args.get("disease")
    confidence = request.args.get("confidence")
    image = request.args.get("image")

    image_path = os.path.join("static/uploads", image)

    info = DISEASE_INFO.get(disease, {
        "desc": "No description available.",
        "remedy": "Consult agricultural expert."
    })

    now = datetime.now().strftime("%d-%m-%Y  %H:%M")

    file_name = "Plant_Health_Report.pdf"

    c = canvas.Canvas(file_name, pagesize=A4)

    # ===== HEADER =====
    c.setFont("Helvetica-Bold", 22)
    c.drawString(120, 810, "🌱 PLANT HEALTH AI REPORT")

    c.setFont("Helvetica", 10)
    c.drawString(400, 795, f"Date: {now}")

    c.line(50, 780, 545, 780)

    # ===== IMAGE =====
    if image and os.path.exists(image_path):
        c.drawImage(image_path, 180, 500, width=250, height=250)

    # ===== DETAILS =====
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 460, "Diagnosis")

    c.setFont("Helvetica", 12)
    c.drawString(60, 430, f"Disease: {disease}")
    c.drawString(60, 405, f"Confidence: {confidence}%")

    # Confidence bar
    bar_width = float(confidence) * 3
    c.setFillColorRGB(0,1,0)
    c.rect(60, 380, bar_width, 12, fill=1)

    c.setFillColorRGB(0,0,0)

    # ===== DESCRIPTION =====
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60, 350, "Description")

    text = c.beginText(60, 325)
    text.setFont("Helvetica", 11)
    text.textLines(info["desc"])
    c.drawText(text)

    # ===== REMEDY =====
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60, 260, "Recommended Remedy")

    text2 = c.beginText(60, 235)
    text2.setFont("Helvetica", 11)
    text2.textLines(info["remedy"])
    c.drawText(text2)

    # ===== FOOTER =====
    c.line(50, 80, 545, 80)
    c.setFont("Helvetica", 9)
    c.drawString(200, 60, "Generated by Plant Health AI System")

    c.save()

    return send_file(file_name, as_attachment=True)

# ---------------- RUN ----------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)