import cv2
import os
import sys

# Ensure Haar cascade is available (download if missing)
HAAR_FILE = 'haarcascade_frontalface_default.xml'
if not os.path.exists(HAAR_FILE):
    try:
        import urllib.request
        url = (
            'https://raw.githubusercontent.com/opencv/opencv/master/'
            'data/haarcascades/haarcascade_frontalface_default.xml'
        )
        print('Downloading Haar cascade...')
        urllib.request.urlretrieve(url, HAAR_FILE)
        print('Downloaded', HAAR_FILE)
    except Exception as e:
        print('Failed to download Haar cascade:', e)
        sys.exit(1)

# Load cascade
face_cascade = cv2.CascadeClassifier(HAAR_FILE)
if face_cascade.empty():
    print('Failed to load cascade classifier from', HAAR_FILE)
    sys.exit(1)

# Open default webcam (0). Change the index if you have multiple cameras.
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open webcam (index 0). Trying index 1...')
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print('Cannot open any webcam. Exiting.')
        sys.exit(1)

print("Face Detection Started. Press 'ESC' to quit...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read frame from webcam. Exiting loop.')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces (tune scaleFactor/minNeighbors for your camera/lighting)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    print('Face Detection stopped successfully')
