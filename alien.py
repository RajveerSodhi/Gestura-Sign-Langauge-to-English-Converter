from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import time
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("Model_Alien/keras_Model.h5", compile=False)

# Load the labels
class_names = open("Model_Alien/labels.txt", "r").readlines()

#Morse code string
morse = ""
spaceAdded = False
delay = 3000  # ms
last_time = time.time()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    image_hands = image.copy()
    hands, _ = detector.findHands(image_hands)

    if hands:
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
            morse += class_name[2]
            last_time = current_time
            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
            spaceAdded = False
    else:
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imshow("Webcam Image", image)
        # current_time = time.time()
        if not spaceAdded:
            morse += " "
            spaceAdded = True
        print(morse)
        print(hands)
        # last_time = current_time

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to encrypt the string according to the morse code chart
def encrypt(message):
    cypher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cypher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cypher += ' '
 
    return cypher
 
# Function to decrypt the string from morse to english
def decrypt(message):
    message += ' '
 
    decypher = ''
    ctext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            ctext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decypher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decypher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(ctext)]
                ctext = ''
 
    return decypher
 
# Hard-coded driver function to run the program
def main():
    # message = "HELLO WORLD"
    # result = encrypt(message.upper())
    # print (result)
 
    # message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ..."
    # CAT = -.-. .- - ... -....- .- .-. . -....- -.-. ..- - .
    result = decrypt(morse)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()
