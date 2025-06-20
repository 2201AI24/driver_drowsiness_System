# 💤 Driver Drowsiness Detection System

A real-time, deep learning–powered application that detects driver fatigue by monitoring eye closure and yawning through webcam input. This system is designed to enhance road safety by triggering alerts and saving logs when signs of drowsiness are detected.

## 🚀 Features

- 🧠 **CNN-Based Detection**  
  Two custom-trained Convolutional Neural Network (CNN) models classify eye states (open/closed) and mouth states (yawn/no yawn).

- 🎯 **Facial Landmark Detection with Mediapipe**  
  Uses Mediapipe's FaceMesh to accurately extract eye and mouth regions from webcam frames.

- ⚙️ **Smart Frame-Based Logic**  
  Triggers drowsiness alerts if:
  - Eyes are closed for more than 15 consecutive frames
  - Yawning is detected in 2 or more consecutive frames

- 💾 **Event Logging & Screenshots**  
  Automatically saves detection logs (with timestamps) and screenshots of drowsiness events.

- 🌐 **Interactive Streamlit Web App**  
  A clean and user-friendly UI with real-time video, status indicators, and downloadable event logs.

## 🛠️ Tech Stack

- **Languages**: Python  
- **Libraries**: TensorFlow, OpenCV, Mediapipe, Streamlit, NumPy, Pandas  
- **Models**: Custom CNNs (Keras `.h5` format)

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/driver_drowsiness_System.git
cd driver_drowsiness_System
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy
Edit
pip install streamlit opencv-python mediapipe tensorflow pandas
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
```
This will open a new tab in your browser.

Click the Start Detection button to begin real-time monitoring.

Click Stop Detection to stop the webcam feed.

Download logs from the sidebar after detection.

📂 Project Structure
bash
Copy
Edit
driver_drowsiness_System/
├── app.py                       # Main Streamlit app
├── eye_state_model.h5          # CNN model for eye state classification
├── yawn_detection_model.h5     # CNN model for yawn detection
├── drowsiness_logs/
│   ├── screenshots/            # Saved frames of detected events
│   └── drowsiness_log.csv      # Log file with timestamps and filenames
├── README.md                   # Project description
📸 Screenshots
Real-Time Detection	Drowsiness Alert

(Replace the image paths with your actual screenshots in the static/ folder if you include them)

📈 Future Improvements
🔊 Add sound/vibration alerts

📱 Deploy as mobile app or executable GUI

🎥 Head pose detection for distraction monitoring

🤖 Combine eye and yawn detection into a multi-task CNN

☁️ Cloud deployment or Edge device integration (Jetson Nano / Raspberry Pi)

📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Metla Umesh Chandra
📧 2201AI24@iitp.ac.in
🌐 LinkedIn | GitHub
