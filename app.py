"""
Plant Disease Detection Flask Application
Uses MobileNetV2 model for image classification
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from flask import send_file
from flask import Flask, render_template, request, jsonify, url_for
import os
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import json

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model
MODEL_PATH = 'Mobilenetv2.h5'
try:
    model = load_model(MODEL_PATH)
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None

# Class names for plant diseases
# Update these based on your actual model's training classes
CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]
DISEASE_INFO = {
    "Apple - Black rot": {
        "desc": "Black rot is a fungal disease causing dark lesions on leaves and fruits.",
        "remedy": "Remove infected leaves, apply fungicide, and ensure proper air circulation."
    }
}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def preprocess_image(img_path):
    try:
        img = Image.open(img_path).convert("RGB")

        # Resize to model input size
        img = img.resize((256, 256))

        # Convert to numpy
        img_array = np.array(img)

        # Normalize
        img_array = img_array / 255.0

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        return img_array

    except Exception as e:
        print("Preprocessing error:", e)
        return None


def predict_disease(img_path):
    """
    Predict plant disease from image
    """

    if model is None:
        raise Exception("Model not loaded properly")

    try:
        # Preprocess image
        processed_img = preprocess_image(img_path)

        if processed_img is None:
            raise Exception("Image preprocessing failed")

        # Make prediction (silent mode)
        predictions = model.predict(processed_img, verbose=0)

        predicted_class_index = int(np.argmax(predictions))
        confidence = float(np.max(predictions)) * 100

        # Get class label
        predicted_class = CLASS_NAMES[predicted_class_index]

        # Format label nicely
        disease_name = predicted_class.replace("___", " - ").replace("_", " ")

        return {
            "disease": disease_name,
            "confidence": round(confidence, 2),
            "class_index": predicted_class_index
        }

    except Exception as e:
        print("Prediction error:", e)
        return {
            "disease": "Prediction Failed",
            "confidence": 0,
            "class_index": -1
        }


@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return redirect('/')

    file = request.files['file']

    if file.filename == '':
        return redirect('/')

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    result = predict_disease(filepath)

    info = DISEASE_INFO.get(result["disease"], {
        "desc": "No description available.",
        "remedy": "Consult agricultural expert."
    })

    return render_template(
        "result.html",
        disease=result["disease"],
        confidence=result["confidence"],
        image=filename,
        description=info["desc"],
        remedy=info["remedy"]
    )


@app.route('/result')
def result():
    """Render the result page"""
    return render_template('result.html')

@app.route('/download_report')
def download_report():
    file_path = "report.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)
    c.drawString(100, 800, "Plant Disease Detection Report")
    c.drawString(100, 760, f"Disease: {request.args.get('disease')}")
    c.drawString(100, 730, f"Confidence: {request.args.get('confidence')}%")
    c.drawString(100, 700, f"Description: {request.args.get('desc')}")
    c.drawString(100, 670, f"Remedy: {request.args.get('remedy')}")

    c.save()

    return send_file(file_path, as_attachment=True)


@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File is too large. Maximum size is 16MB'}), 413


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('index.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Check if model file exists
    if not os.path.exists(MODEL_PATH):
        print(f"⚠ Warning: Model file '{MODEL_PATH}' not found!")
        print("Please ensure Mobilenetv2.h5 is in the same directory as app.py")

    # Run the Flask app
    print("="*50)
    print("🌱 Plant Disease Detection System")
    print("="*50)
    app.run(debug=True, host='0.0.0.0', port=5000)
