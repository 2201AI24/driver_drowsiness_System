# 🧠 Driver Drowsiness Detection – Dataset Branch

This branch contains the **training dataset** used for the Driver Drowsiness Detection system. It includes categorized images of:

- 👁️ **Open eyes**
- 😴 **Closed eyes**
- 😶 **No yawn**
- 😮 **Yawning**

---

## 📂 Folder Structure
---
train/
├── Closed/       # Images with closed eyes
├── Open/         # Images with open eyes
├── no_yawn/      # Images without yawning
└── yawn/         # Images with visible yawns
---

## 📦 Purpose of This Branch

This branch was created **separately** from the main code branch to:

- Keep large dataset files out of the `main` branch
- Maintain a clean separation between **code** and **data**
- Allow users to **download only the dataset**, if needed

---

## 📥 How to Use This Dataset

### ✅ Option 1: Download ZIP

Click the green **`<> Code`** button above → then **`Download ZIP`**.

Unzip it and place the `train/` folder into your project directory.

### ✅ Option 2: Use Git to pull this branch only

```bash
git clone --branch upload-train-folder https://github.com/2201AI24/driver_drowsiness_System.git
```
## 🔗 Related Code Repository

To see the full project with the app and model code, visit the [`main` branch](https://github.com/2201AI24/driver_drowsiness_System/tree/main):

- 🧑‍💻 Real-time webcam-based drowsiness detection  
- 🧠 CNN models for eye state and yawning detection  
- 📸 Screenshot logging and CSV event recording  
- ⚠️ Visual alerts for detected drowsiness  

---

## 👤 Author

**Metla Umesh Chandra**  
🎓 B.Tech in AI & Data Science – IIT Patna  
📧 2201AI24@iitp.ac.in  
🌐 GitHub: [@2201AI24](https://github.com/2201AI24)  
🔗 LinkedIn: [metla-umesh-chandra](https://www.linkedin.com/in/metla-umesh-chandra)

---

> ⚠️ This dataset is used for academic and learning purposes only. Please use it ethically and responsibly.
