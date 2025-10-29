# Final Year Project - Face Detection / Dataset Collection

This folder contains two simple OpenCV scripts used for face dataset collection and real-time face detection.

Files:
- `faceDataset.py` - captures 30 grayscale face images into `dataset/champ` (automatically downloads Haar cascade if missing).
- `FaceDetection.py` - real-time face detection using Haar cascade; displays webcam feed and outlines detected faces.

Quick start (Windows PowerShell):

1. Create and activate a suitable Python environment (optional but recommended).
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run dataset collection:

```powershell
python faceDataset.py
```

4. Run live detection:

```powershell
python FaceDetection.py
```
