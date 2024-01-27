import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
width = 265
height = 26
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["D", "A", "C", "B", "E", "F", "I", "T", "O", "N", "S", "H", "R", "M", "L"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
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