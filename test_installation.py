"""
Installation Test Script
Run this script to verify your setup is correct
"""

import sys

print("=" * 60)
print("🧪 Plant Disease Detection - Installation Test")
print("=" * 60)
print()

# Test 1: Python Version
print("✓ Testing Python version...")
python_version = sys.version_info
if python_version.major >= 3 and python_version.minor >= 8:
    print(f"  ✓ Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK")
else:
    print(f"  ✗ Python version too old: {python_version.major}.{python_version.minor}")
    print("  Please upgrade to Python 3.8 or higher")
    sys.exit(1)

print()

# Test 2: Required Modules
print("✓ Testing required modules...")
required_modules = {
    'flask': 'Flask',
    'tensorflow': 'TensorFlow',
    'PIL': 'Pillow',
    'numpy': 'NumPy',
    'werkzeug': 'Werkzeug'
}

missing_modules = []
for module, name in required_modules.items():
    try:
        __import__(module)
        print(f"  ✓ {name} - Installed")
    except ImportError:
        print(f"  ✗ {name} - Missing")
        missing_modules.append(name)

if missing_modules:
    print()
    print("❌ Missing modules detected!")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

print()

# Test 3: Model File
print("✓ Testing model file...")
import os
if os.path.exists('Mobilenetv2.h5'):
    file_size = os.path.getsize('Mobilenetv2.h5') / (1024 * 1024)  # Convert to MB
    print(f"  ✓ Mobilenetv2.h5 found ({file_size:.2f} MB)")
else:
    print("  ✗ Mobilenetv2.h5 not found!")
    print("  Please ensure the model file is in the project root directory")
    sys.exit(1)

print()

# Test 4: Model Loading
print("✓ Testing model loading...")
try:
    from tensorflow.keras.models import load_model
    model = load_model('Mobilenetv2.h5')
    print("  ✓ Model loaded successfully")
    print(f"  ✓ Model input shape: {model.input_shape}")
    print(f"  ✓ Model output shape: {model.output_shape}")
except Exception as e:
    print(f"  ✗ Error loading model: {e}")
    sys.exit(1)

print()

# Test 5: Directory Structure
print("✓ Testing directory structure...")
required_dirs = ['templates', 'static', 'static/css', 'static/js']
required_files = [
    'app.py',
    'templates/index.html',
    'templates/result.html',
    'static/css/style.css',
    'static/js/script.js'
]

for directory in required_dirs:
    if os.path.isdir(directory):
        print(f"  ✓ Directory '{directory}' - OK")
    else:
        print(f"  ✗ Directory '{directory}' - Missing")

for file in required_files:
    if os.path.isfile(file):
        print(f"  ✓ File '{file}' - OK")
    else:
        print(f"  ✗ File '{file}' - Missing")

print()

# Test 6: Flask App
print("✓ Testing Flask application...")
try:
    from app import app
    print("  ✓ Flask app imported successfully")
except Exception as e:
    print(f"  ✗ Error importing Flask app: {e}")
    sys.exit(1)

print()

# All tests passed
print("=" * 60)
print("🎉 All tests passed! Your installation is ready.")
print("=" * 60)
print()
print("To start the application, run:")
print("  python app.py")
print()
print("Then open your browser to:")
print("  http://localhost:5000")
print()
print("=" * 60)
