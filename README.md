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

Notes:
- The scripts will attempt to download `haarcascade_frontalface_default.xml` if it is not present in the folder.
- Collected images are saved under `dataset/champ`. The `.gitignore` excludes that folder by default so captured images are not committed.

How to push this project to GitHub (example):

```powershell
cd "c:\Users\Manjunath\OneDrive\DA PROJECTS\Final_year_project\Day5_Code"
# Initialize repo (if not already)
git init
# Add remote (replace <your-repo-url> with the URL you create on GitHub)
git remote add origin <your-repo-url>
# Push to GitHub
git push -u origin main
```

If you'd like, I can run the local git init/commit step for you now and then you can provide the remote URL so I can push (I won't push without the remote and your consent).