import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
width = 224
height = 244
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["A","B","C"]

while True:
    success, img = cap.read()

    prediction, index = classifier.getPrediction(img, draw=False)
    cv2.putText(img, labels[index], (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
    cv2.imshow("Image", img)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()