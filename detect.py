import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
width = 265
height = 26
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["D", "A", "C", "B", "E", "F", "I", "T", "O", "N", "S", "H", "R", "M", "L"]
res = ""

# Set the delay to 3 seconds (3000 milliseconds)
delay = 3  # seconds
last_time = time.time()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("Image", img)

    current_time = time.time()
    # Run the classifier every 3 seconds
    if current_time - last_time >= delay:
        imgOutput = img.copy()
        prediction, index = classifier.getPrediction(img, draw=False)
        print(prediction, index)
        cv2.putText(imgOutput, labels[index], (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        res += labels[index]

        cv2.imshow("Image", imgOutput)
        last_time = time.time()  # Update the last time

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

from gtts import gTTS
import os

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=res, lang=language, slow=False)

# Saving the converted audio in a file
tts.save("output.mp3")

# Playing the converted file on macOS
os.system("open output.mp3")

print(res)
