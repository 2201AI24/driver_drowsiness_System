import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import os
import datetime
import pandas as pd

st.set_page_config(page_title="Driver Drowsiness Detection", layout="centered")

# Load models
@st.cache_resource
def load_models():
    return load_model('eye_state_model.h5'), load_model('yawn_detection_model.h5')

eye_model, yawn_model = load_models()

# Mediapipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Landmark indices
LEFT_EYE_IDX = [33, 133]
RIGHT_EYE_IDX = [362, 263]
MOUTH_IDX = [13, 14]

# Preprocessing helper
def get_roi_from_landmarks(image, landmarks, indices, margin=20):
    h, w = image.shape[:2]
    pts = np.array([[int(landmarks[i].x * w), int(landmarks[i].y * h)] for i in indices])
    x_min, y_min = np.min(pts, axis=0) - margin
    x_max, y_max = np.max(pts, axis=0) + margin
    x_min, y_min = max(0, x_min), max(0, y_min)
    x_max, y_max = min(w, x_max), min(h, y_max)
    return image[y_min:y_max, x_min:x_max]

def preprocess(img):
    if img.size == 0:
        return None
    img = cv2.resize(img, (64, 64))
    img = img.astype('float32') / 255.0
    return np.expand_dims(img, axis=0)

# UI Elements
st.title("😴 Real-Time Drowsiness Detection")
st.markdown("Click **Start Detection** to begin webcam-based monitoring.")

start_button = st.button("▶️ Start Detection")
stop_button = st.button("⏹️ Stop Detection")

# Session state for webcam run control
if "run_detection" not in st.session_state:
    st.session_state.run_detection = False

if "eye_counter" not in st.session_state:
    st.session_state.eye_counter = 0

if "yawn_counter" not in st.session_state:
    st.session_state.yawn_counter = 0

if start_button:
    st.session_state.run_detection = True

if stop_button:
    st.session_state.run_detection = False

# Create folders if needed
if not os.path.exists("drowsiness_logs"):
    os.makedirs("drowsiness_logs/screenshots")
    with open("drowsiness_logs/drowsiness_log.csv", "w") as f:
        f.write("timestamp,filename\n")

# Sidebar Download Button
st.sidebar.title("📥 Logs")
if os.path.exists("drowsiness_logs/drowsiness_log.csv"):
    with open("drowsiness_logs/drowsiness_log.csv", "r") as f:
        csv = f.read()
    st.sidebar.download_button("Download Log CSV", csv, "drowsiness_log.csv", "text/csv")
else:
    st.sidebar.info("No logs yet.")

# Run Detection
if st.session_state.run_detection:
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while st.session_state.run_detection:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark

            # Eye detection
            eye_closed = False
            for eye_idx in [LEFT_EYE_IDX, RIGHT_EYE_IDX]:
                eye_img = get_roi_from_landmarks(frame, landmarks, eye_idx)
                processed = preprocess(eye_img)
                if processed is not None:
                    pred = eye_model.predict(processed, verbose=0)[0][0]
                    if pred < 0.5:
                        eye_closed = True

            if eye_closed:
                st.session_state.eye_counter += 1
            else:
                st.session_state.eye_counter = 0

            # Yawn detection
            mouth_img = get_roi_from_landmarks(frame, landmarks, MOUTH_IDX, margin=30)
            processed = preprocess(mouth_img)
            if processed is not None:
                pred = yawn_model.predict(processed, verbose=0)[0][0]
                if pred < 0.5:
                    st.session_state.yawn_counter += 1
                else:
                    st.session_state.yawn_counter = 0

            # Trigger alert condition
            if st.session_state.eye_counter > 15 or st.session_state.yawn_counter >= 2:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"drowsiness_logs/screenshots/drowsy_{timestamp}.jpg"
                cv2.imwrite(filename, frame)

                with open("drowsiness_logs/drowsiness_log.csv", "a") as f:
                    f.write(f"{timestamp},{filename}\n")

                cv2.putText(frame, "DROWSINESS DETECTED!", (50, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            else:
                cv2.putText(frame, "ACTIVE", (50, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Show counter on screen
            cv2.putText(frame, f"Eye Frames: {st.session_state.eye_counter}", (10, 420),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Yawn Frames: {st.session_state.yawn_counter}", (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        else:
            cv2.putText(frame, "NO FACE DETECTED", (50, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()
    st.success("✅ Webcam stopped.")
