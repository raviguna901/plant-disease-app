# 📦 Complete Setup Instructions

## Before You Start

You need the **Mobilenetv2.h5** model file. Make sure you have this file ready before proceeding.

---

## Step-by-Step Setup

### 1. Download or Extract the Project

Extract the PlantDiseaseApp folder to your desired location.

### 2. Place the Model File

**IMPORTANT**: Copy your `Mobilenetv2.h5` file into the PlantDiseaseApp folder.

Your folder structure should look like:
```
PlantDiseaseApp/
├── app.py
├── Mobilenetv2.h5          ← Place your model here!
├── requirements.txt
├── templates/
└── static/
```

### 3. Open Terminal/Command Prompt

Navigate to the PlantDiseaseApp folder:

**Windows:**
```bash
cd path\to\PlantDiseaseApp
```

**Mac/Linux:**
```bash
cd path/to/PlantDiseaseApp
```

### 4. Install Python Dependencies

Run the following command:
```bash
pip install -r requirements.txt
```

**This will install:**
- Flask (web framework)
- TensorFlow (deep learning)
- Pillow (image processing)
- NumPy (numerical operations)
- Werkzeug (utilities)

**Note**: Installation may take 5-10 minutes depending on your internet speed.

### 5. Verify Installation (Optional)

Run the test script:
```bash
python test_installation.py
```

This will check if everything is installed correctly.

### 6. Run the Application

Start the Flask server:
```bash
python app.py
```

You should see output like:
```
✓ Model loaded successfully!
==================================================
🌱 Plant Disease Detection System
==================================================
 * Running on http://0.0.0.0:5000
```

### 7. Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

---

## Using Virtual Environment (Recommended)

Virtual environments keep your project dependencies isolated.

### Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Your terminal prompt should now show `(venv)` at the beginning.

### Install Dependencies in Virtual Environment

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Deactivate Virtual Environment (When Done)

```bash
deactivate
```

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 7+, macOS 10.12+, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB (8GB recommended)
- **Storage**: 2GB free space
- **Internet**: Required for initial setup

### Python Installation

Don't have Python? Download from:
- **Official Website**: https://www.python.org/downloads/
- **Windows**: Download installer and check "Add Python to PATH"
- **Mac**: Use Homebrew: `brew install python3`
- **Linux**: Usually pre-installed, or use: `sudo apt install python3`

---

## Troubleshooting

### Problem: "python: command not found"

**Solution**: Install Python or use `python3` instead of `python`

### Problem: "pip: command not found"

**Solution**:
- Try `python -m pip` instead of `pip`
- Or install pip: `python -m ensurepip --upgrade`

### Problem: Permission Denied

**Solution**: Use `pip install --user -r requirements.txt`

### Problem: TensorFlow Installation Fails

**Solutions**:
1. Update pip: `pip install --upgrade pip`
2. Install specific version: `pip install tensorflow==2.15.0`
3. For older systems, try: `pip install tensorflow-cpu==2.15.0`

### Problem: Model File Not Found

**Solution**:
- Verify `Mobilenetv2.h5` is in the same folder as `app.py`
- Check file name spelling (case-sensitive on Linux/Mac)

### Problem: Port 5000 Already in Use

**Solution**:
Edit `app.py` (line 149) to use different port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Then access at: http://localhost:5001

### Problem: Module Import Errors

**Solution**:
```bash
pip uninstall tensorflow flask pillow numpy werkzeug
pip install -r requirements.txt
```

---

## Running on Different Platforms

### Windows
- Use Command Prompt or PowerShell
- Paths use backslash: `C:\Users\YourName\PlantDiseaseApp`
- Run: `python app.py`

### macOS
- Use Terminal
- May need to use `python3` instead of `python`
- Run: `python3 app.py`

### Linux (Ubuntu/Debian)
- Use Terminal
- Install Python venv: `sudo apt install python3-venv`
- Run: `python3 app.py`

---

## Deployment Options

### Local Network Access

Change in `app.py`:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

Access from other devices using your computer's IP:
```
http://192.168.1.XX:5000
```

### Production Deployment

For production use:
1. Set `debug=False`
2. Use proper web server (Gunicorn, uWSGI)
3. Set up HTTPS
4. Configure firewall
5. Use environment variables for sensitive data

**Example with Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## File Upload Limits

Default maximum file size: **16MB**

To change, edit `app.py` (line 21):
```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

---

## Security Notes

- File type validation: Only JPG, JPEG, PNG allowed
- Secure filename handling prevents directory traversal
- File size limits prevent DoS attacks
- Input sanitization included

For production:
- Use HTTPS
- Add authentication
- Rate limiting
- Proper error logging
- Regular security updates

---

## Getting Help

1. **Read the full README.md** for detailed information
2. **Run test_installation.py** to diagnose issues
3. **Check error messages** in terminal for clues
4. **Google the error** with "Flask" or "TensorFlow"

---

## Next Steps After Setup

1. ✅ Upload a test plant image
2. ✅ Verify predictions work correctly
3. ✅ Test on different plant diseases
4. ✅ Check mobile responsiveness
5. ✅ Customize for your needs

---

## Customization

### Change Class Names
Edit `CLASS_NAMES` list in `app.py` (line 28-67)

### Modify UI Colors
Edit `static/css/style.css` (search for color codes)

### Add More Features
- Treatment recommendations
- History tracking
- User authentication
- Email reports

---

## Performance Tips

- Close unnecessary applications
- Use SSD for faster file operations
- Increase RAM allocation if available
- Use CPU-only TensorFlow on older machines

---

## Support

- 📖 Full Documentation: `README.md`
- 🚀 Quick Start: `QUICK_START.md`
- 🧪 Test Setup: `python test_installation.py`

---

**Ready to start? Follow the 7 steps above!** 🌱

---

Last Updated: 2024
