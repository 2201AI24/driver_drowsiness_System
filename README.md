# 💤 Driver Drowsiness Detection System

A real-time computer vision system that detects driver fatigue by monitoring eye closure and yawning using webcam input. The system leverages deep learning models to trigger alerts and log drowsiness events, helping reduce road accidents.

---

## 🔍 Overview

This project implements a **real-time driver drowsiness detection system** using:

- ✅ Convolutional Neural Networks (CNNs) for eye and yawn state classification  
- ✅ Mediapipe FaceMesh for accurate facial landmark detection  
- ✅ Streamlit interface for interactive user control and visualization

The system analyzes live webcam feed to identify fatigue signs such as prolonged eye closure and frequent yawning. Alerts are triggered and screenshots/logs are saved when drowsiness is detected.

---

## 📌 Features

- 🧠 Real-time eye and yawn detection using custom CNN models  
- 🎯 FaceMesh landmark tracking to extract eyes and mouth regions  
- 🕒 Frame-based alert logic with counters to reduce false positives  
- 💾 Automatic screenshot saving and log entry when drowsiness is detected  
- 🌐 Streamlit web app with Start/Stop controls and log download

---

## 📂 Project Structure

```bash
driver_drowsiness_System/
├── app.py # Main Streamlit application
├── eye_state_model.h5 # Trained CNN model for eye state classification
├── yawn_detection_model.h5 # Trained CNN model for yawn detection
├── drowsiness_logs/
│ ├── screenshots/ # Saved images when drowsiness is detected
│ └── drowsiness_log.csv # Timestamped log of all detection events
├── README.md # Project documentation

```

## ⚙️ Installation

### ✅ Prerequisites

- Python 3.7 or higher
- Webcam-enabled environment

### 🔧 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/driver_drowsiness_System.git
cd driver_drowsiness_System

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```
## 🧠 How It Works

### 🔹 Face Detection & ROI Extraction
Mediapipe detects facial landmarks and crops regions for both eyes and the mouth.

### 🔹 CNN-Based Classification
- Eye model predicts **Open** or **Closed** from cropped eye images  
- Yawn model predicts **Yawn** or **No Yawn** from mouth region

### 🔹 Alert Logic
If eyes remain closed for **≥ 15 frames** or yawns are detected in **≥ 2 frames**, the system:
- Saves the current frame as a screenshot  
- Logs the event with a timestamp and reason  
- Displays an alert message in the UI

### 🔹 User Interface
- Start/Stop webcam detection  
- Live counter updates for eyes/yawn  
- CSV log download from sidebar

---

## 📸 Screenshots


---

## 📚 Tech Stack

- **Frontend**: Streamlit  
- **Computer Vision**: OpenCV, Mediapipe  
- **Deep Learning**: TensorFlow / Keras (CNN)  
- **Utilities**: Pandas, NumPy, OS  

---

## 🚀 Future Enhancements

- 🔊 Add audio alert for drowsiness detection  
- 📱 Convert to mobile app or standalone desktop executable  
- 🎥 Add head pose tracking for enhanced detection  
- 🧠 Merge eye and yawn into a multi-output CNN  
- ☁️ Deploy on Jetson Nano or Raspberry Pi for in-vehicle use  

---

## 🙌 Acknowledgments

- [Mediapipe by Google](https://github.com/google/mediapipe) for real-time landmark tracking  
- OpenCV & TensorFlow open-source communities  
- Public datasets used for training eye and yawn classifiers  

---

## 📬 Contact

**Metla Umesh Chandra**  
📧 Email: [2201AI24@iitp.ac.in](mailto:2201AI24@iitp.ac.in)  
🐙 GitHub: [@2201AI24](https://github.com/2201AI24)  
🔗 LinkedIn: [metla-umesh-chandra](https://www.linkedin.com/in/metla-umesh-chandra/)  

---

> ⚠️ This is an academic project built for learning and demonstration purposes. Please use responsibly and ethically.

