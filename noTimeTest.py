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
import os
import sys
from language import change_language
from speech import text_to_speech

lang = sys.argv[1]

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Load the model
model = load_model(os.path.join(script_directory, "Model_RJ/keras_model.h5"), compile=False)


# Load the labels
class_names = open(os.path.join(script_directory, "Model_RJ/labels.txt"), "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

res = ""

# Set the delay to 3 seconds (3000 milliseconds)
delay = 3000  # ms
last_time = time.time()

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    current_time = time.time()
    
    if current_time - last_time >= delay / 1000:
        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        res += class_name[2]
        # print("Class:", class_name[2:], end="")
        # print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        last_time = current_time
        print(class_name[2])


    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 32 is the ASCII for the space bar on your keyboard.
    if keyboard_input == 32 :
        break

camera.release()
cv2.destroyAllWindows()

from gtts import gTTS
import os

print(res)
text_to_speech(res,lang)

