## 👨‍💻 Real-Time Face Recognition System

This project demonstrates a **real-time face recognition system** built using **OpenCV** and the **Local Binary Pattern Histograms (LBPH)** algorithm for efficient face detection and classification.

---

### 🚀 Overview

The system functions in three core phases, each handled by an individual Python script:

| **Script Name**       | **Description**                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **faceDataset.py**    | Captures 30 grayscale images per user and stores them in the `dataset/champ` directory. Automatically downloads the Haar Cascade classifier if not already available.                 |
| **faceTrainer.py**    | Trains the LBPH face recognition model using the collected dataset and saves the trained model as `trainer/trainer.yml`.                                                              |
| **faceRecognizer.py** | Loads the trained model (`trainer/trainer.yml`), starts real-time video capture, detects faces, and displays the **recognized ID** and **confidence score** above each detected face. |

---

### ⚙️ Execution Steps

1. **Capture Face Data**
   Run `faceDataset.py` to collect and store grayscale face samples.

2. **Train the Model**
   Execute `faceTrainer.py` to train the LBPH model and generate the recognition file.

3. **Run Real-Time Recognition**
   Launch `faceRecognizer.py` to start the webcam-based recognition process. The system will display live results with detected faces and recognition confidence.

---

### 💡 Key Features

* Automated dataset creation and model training
* Real-time face detection and recognition
* Confidence-based face identification
* Lightweight and easy to set up using OpenCV

---

