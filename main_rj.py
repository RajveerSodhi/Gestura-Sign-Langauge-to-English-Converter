import cv2
from cvzone.HandTrackingModule import HandDetector
from gtts import gTTS
import os
import urllib3
import threading

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
previous_text = ""
lock = threading.Lock()
audio_file_counter = 0  # Counter for generating unique audio file names

def process_audio(text):
    global audio_file_counter

    try:
        tts = gTTS(text=text, lang='en')
        audio_file_name = f"output_{audio_file_counter}.mp3"
        tts.save(audio_file_name)
        os.system(f"afplay {audio_file_name}")
        audio_file_counter += 1
    except Exception as e:
        print(f"Error processing audio: {e}")

def main():
    global previous_text

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        current_text = ""  # Default empty string if no hand is detected

        if hands:
            current_text = hands[0]["type"]

        # Check if there's a change in hand gesture
        if current_text != previous_text and current_text:
            with lock:
                threading.Thread(target=process_audio, args=(current_text,)).start()
            previous_text = current_text

        cv2.imshow('img', img)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Execution interrupted by the user.")
    finally:
        cap.release()
        cv2.destroyAllWindows()
