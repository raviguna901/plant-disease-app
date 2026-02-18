import gradio as gr
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

MODEL_PATH = "Mobilenetv2.h5"

model = load_model(MODEL_PATH)

CLASS_NAMES = [
    'Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy',
    'Blueberry___healthy','Cherry___Powdery_mildew','Cherry___healthy',
    'Corn___Cercospora_leaf_spot','Corn___Common_rust','Corn___Northern_Leaf_Blight','Corn___healthy',
    'Grape___Black_rot','Grape___Esca','Grape___Leaf_blight','Grape___healthy',
    'Orange___Citrus_greening','Peach___Bacterial_spot','Peach___healthy',
    'Pepper___Bacterial_spot','Pepper___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy',
    'Raspberry___healthy','Soybean___healthy','Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch','Strawberry___healthy',
    'Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight','Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot','Tomato___Spider_mites','Tomato___Target_Spot',
    'Tomato___Yellow_Leaf_Curl','Tomato___Mosaic_virus','Tomato___healthy'
]

def predict(image):
    image = image.resize((256,256)).convert("RGB")
    arr = np.array(image)/255.0
    arr = np.expand_dims(arr,0)

    preds = model.predict(arr)
    idx = np.argmax(preds)
    conf = float(np.max(preds))*100

    disease = CLASS_NAMES[idx].replace("___"," - ").replace("_"," ")

    if conf < 70:
        return "❌ Upload clear plant leaf image"

    return f"Disease: {disease}\nConfidence: {conf:.2f}%"

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="🌱 Plant Disease Detection",
    description="Upload plant leaf image"
).launch(server_name="0.0.0.0", server_port=7860)