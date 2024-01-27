import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
width = 200
height = 200
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["D", "A", "C", "B", "E", "F", "I", "T", "O", "N", "S", "H", "R", "M", "L"]
offset = 20

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        cv2.imshow("ImageCrop", imgCrop)
        imgCrop_resized = cv2.resize(imgCrop, (400, 400))
        cv2.imshow("imgCrop_resized", imgCrop_resized)


    prediction, index = classifier.getPrediction(img, draw=False)
    print(prediction, index)
    cv2.putText(imgOutput, labels[index], (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
    cv2.imshow("Image", imgOutput)
    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()