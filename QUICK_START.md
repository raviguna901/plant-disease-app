# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8 or higher installed
- `Mobilenetv2.h5` model file in the project root

## Installation & Running (3 Simple Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## Using the Application

1. **Upload Image**: Drag & drop or click "Browse Files"
2. **Click Analyze**: Press "Analyze Image" button
3. **View Results**: See disease prediction and confidence score

---

## Stopping the Application

Press `Ctrl + C` in the terminal

---

## Troubleshooting

### If you get "ModuleNotFoundError":
```bash
pip install -r requirements.txt
```

### If port 5000 is busy:
Edit `app.py` line 149:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### If model file is missing:
Ensure `Mobilenetv2.h5` is in the same folder as `app.py`

---

## Virtual Environment (Optional but Recommended)

**Create & Activate:**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**Then run steps 1-3 above**

---

## File Structure

```
PlantDiseaseApp/
├── app.py              ← Main application
├── Mobilenetv2.h5      ← Model file (required!)
├── requirements.txt    ← Dependencies
├── README.md           ← Full documentation
├── templates/          ← HTML pages
└── static/             ← CSS, JS, uploads
```

---

## Support

- Full documentation: See `README.md`
- Port conflicts: Change port in `app.py`
- Model errors: Verify `Mobilenetv2.h5` exists

---

**That's it! Start detecting plant diseases! 🌱**
