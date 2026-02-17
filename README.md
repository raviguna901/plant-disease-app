# 🌱 Plant Disease Detection System

A professional web application for detecting plant diseases using deep learning. Built with Flask and TensorFlow, featuring a modern responsive UI with real-time image classification.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🎯 Accurate Detection**: Uses MobileNetV2 deep learning model trained on 38+ plant disease classes
- **📸 Easy Upload**: Drag-and-drop or browse to upload plant images
- **⚡ Real-time Processing**: Instant disease prediction with confidence scores
- **📱 Responsive Design**: Beautiful UI that works on all devices
- **🎨 Modern Interface**: Clean, professional design with smooth animations
- **📊 Detailed Results**: Visual confidence indicators and health status
- **🖨️ Print Results**: Export prediction results for documentation
- **🔒 Secure**: File type and size validation with secure file handling

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **TensorFlow/Keras**: Deep learning model inference
- **Pillow**: Image processing
- **NumPy**: Numerical computations

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Bootstrap 5**: Responsive framework
- **JavaScript**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Typography (Poppins)

## 📁 Project Structure

```
PlantDiseaseApp/
│
├── app.py                      # Flask application (main backend)
├── Mobilenetv2.h5             # Trained model file
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
│
├── templates/
│   ├── index.html            # Home page with upload interface
│   └── result.html           # Results display page
│
└── static/
    ├── css/
    │   └── style.css         # Custom styles
    ├── js/
    │   └── script.js         # Frontend logic
    └── uploads/              # Temporary upload directory (auto-created)
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM recommended for TensorFlow

### Step 1: Clone or Download

Download the project folder or clone the repository:

```bash
cd PlantDiseaseApp
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: TensorFlow installation may take several minutes depending on your internet speed.

### Step 4: Verify Model File

Ensure `Mobilenetv2.h5` is present in the root directory alongside `app.py`.

## 💻 Usage

### Running the Application

1. **Activate virtual environment** (if not already activated):
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. **Start the Flask server**:
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

4. **Upload an image**:
   - Drag and drop a plant image, or
   - Click "Browse Files" to select an image
   - Click "Analyze Image" button

5. **View results**:
   - See the detected disease
   - Check confidence score
   - View health status recommendations

### Stopping the Application

Press `Ctrl + C` in the terminal where the app is running.

## 🧠 Model Information

### Architecture
- **Model**: MobileNetV2
- **Input Size**: 224x224x3 (RGB images)
- **Output Classes**: 38 plant disease categories
- **Framework**: TensorFlow/Keras

### Supported Plant Species
- Apple
- Blueberry
- Cherry
- Corn (Maize)
- Grape
- Orange
- Peach
- Pepper (Bell)
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

### Disease Categories
The model can detect various diseases including:
- Bacterial spots
- Fungal infections (rust, blight, mildew)
- Leaf spots and scorch
- Viral diseases
- Healthy plant identification

## 🔌 API Endpoints

### `GET /`
**Description**: Home page with upload interface
**Response**: HTML page

### `POST /predict`
**Description**: Upload image and get disease prediction
**Content-Type**: `multipart/form-data`
**Parameters**:
- `file`: Image file (JPG, JPEG, PNG)

**Success Response** (200):
```json
{
    "disease": "Tomato - Late blight",
    "confidence": 95.67,
    "class_index": 30,
    "image_url": "/static/uploads/1234_image.jpg"
}
```

**Error Response** (400/500):
```json
{
    "error": "Error message"
}
```

### `GET /result`
**Description**: Results display page
**Response**: HTML page with prediction results

## 📸 Screenshots

### Home Page
Clean and intuitive interface with drag-and-drop upload functionality.

### Upload Interface
- Modern card-based design
- Real-time image preview
- Progress indicators

### Results Page
- Detailed disease information
- Confidence score visualization
- Health status indicators
- Actionable recommendations

## 🔧 Troubleshooting

### Common Issues

**1. Module Import Error**
```
ModuleNotFoundError: No module named 'tensorflow'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

**2. Model Loading Error**
```
Error loading model: Unable to load model
```
**Solution**: Ensure `Mobilenetv2.h5` is in the same directory as `app.py`

**3. Port Already in Use**
```
Address already in use
```
**Solution**: Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

**4. Memory Error**
```
ResourceExhaustedError: OOM when allocating tensor
```
**Solution**: Close other applications or reduce image size

**5. File Upload Error**
```
File is too large
```
**Solution**: Compress image or use smaller file (max 16MB)

### Platform-Specific Notes

**Windows**:
- Use Command Prompt or PowerShell
- Ensure Python is added to PATH

**macOS**:
- May need to install Xcode Command Line Tools
- Use `python3` instead of `python`

**Linux**:
- May need to install `python3-venv` package
- Ensure sufficient permissions for file uploads

## 🎓 Educational Use

This project is ideal for:
- Final year projects
- Machine learning demonstrations
- Web development portfolios
- Agricultural technology showcases
- Deep learning applications

## 🔐 Security Considerations

- File type validation (only JPG, JPEG, PNG allowed)
- File size limits (16MB maximum)
- Secure filename handling with Werkzeug
- Input sanitization
- Error handling for malicious uploads

## 📈 Future Enhancements

Potential improvements:
- [ ] Add treatment recommendations
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Batch image processing
- [ ] User authentication and history
- [ ] Export reports as PDF
- [ ] Integration with agricultural databases
- [ ] Real-time camera capture

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 👨‍💻 Author

**Plant Disease Detection System**
Powered by Deep Learning & TensorFlow

## 📞 Support

For issues and questions:
- Check the Troubleshooting section
- Review closed issues on GitHub
- Contact the development team

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- MobileNetV2 architecture developers
- Bootstrap team for the UI framework
- Plant Village dataset contributors

---

**Made with ❤️ for Agriculture & Technology**

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Access in browser
# http://localhost:5000
```

**Happy Plant Disease Detection! 🌱**
