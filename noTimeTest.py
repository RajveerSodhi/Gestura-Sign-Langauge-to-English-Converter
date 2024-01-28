import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import time
from autocorrect import Speller
import enchant
diction = enchant.Dict("en_US")
from speech import text_to_speech

def fix_text(text):
    # remove leading and trailing spaces
    text = text.strip()

    # remove repeated characters
    for letter in text:
        repeated_sequence = letter * 3
        while repeated_sequence in text:
            text = text.replace(repeated_sequence, letter)

    # run autocorrect
    spell = Speller()
    split_text = text.split()
    for i in range(len(split_text)):
        if not diction.check(split_text[i]):
            split_text[i] = spell(split_text[i])
    text = " ".join(split_text)

    # fix broken words
    split_text = text.split()
    for i in range(len(split_text) - 1):
        try_combination = split_text[i] + split_text[i + 1]
        if len(split_text[i]) > 0 and len(split_text[i + 1]) > 0 and diction.check(try_combination):
            split_text[i] = try_combination
            split_text[i + 1] = ""

    text = " ".join(split_text)

      # remove extra spaces
    text = " ".join(text.split())


    return text

# Set the delay to 3 seconds (3000 milliseconds)
delay = 4
last_time = time.time()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("Model_SJ/keras_Model.h5", compile=False)

# Load the labels
class_names = open("Model_SJ/labels.txt", "r").readlines()

detector = HandDetector(maxHands=1)

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

res = ""
result = ""
prev_char = ""

while True:
    current_time = time.time()
    # Grab the webcamera's image for model.
    ret, image = camera.read()
    imageCopy = image.copy()
    hands, _ = detector.findHands(imageCopy)
    imageCopy = cv2.resize(imageCopy, (700, 500))
    cv2.putText(imageCopy, "Letter: " + prev_char, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image Display", imageCopy)

    if current_time - last_time >= delay:

        if hands:

            # Resize the raw image into (224-height,224-width) pixels
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

            cv2.imshow("Model Image", image)

            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

            # Predicts the model
            prediction = model.predict(image)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2], end=" ")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            prev_char = class_name[2]
            res += class_name[2]
            cv2.putText(imageCopy, "Letter: " + prev_char, (20, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)



        else:
            res += " "
            print("space")
            cv2.putText(imageCopy, "Letter: " + "space", (20, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        last_time = current_time  # Update the last time

    

    # Exit the loop if 'q', 'j', 'f', 'o', 'r', or spacebar is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('j') or key == ord('f') or key == ord('o') or key == 32:
        break

result = fix_text(res)    

camera.release()
cv2.destroyAllWindows()

from gtts import gTTS
import os

print("Result is: " + result)
text_to_speech(result,"english")
