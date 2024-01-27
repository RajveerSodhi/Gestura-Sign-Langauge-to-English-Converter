import cv2  
import mediapipe as mp
# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
# Initialize video capture
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if not cap.isOpened():
    print("Unable to open camera")
    exit()
# Initialize Mediapipe Hands object
with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:
    while True:
        # Read the frame from the video capture
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame from camera")
            break
        # Convert the frame to RGB for Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the frame with Mediapipe
        results = hands.process(frame_rgb)
        # Draw hand landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2))
                
                h, w, _ = frame.shape #h = frame height , w = frame width 
                x, y = int(hand_landmarks.landmark[12].x * w), int(hand_landmarks.landmark[12].y * h)
                x1, y1 = int(hand_landmarks.landmark[9].x * w), int(hand_landmarks.landmark[9].y * h)

                if y < y1:
                    hand_status = "Open"
                    cv2.rectangle(frame, (0, 0), (200, 60), (255, 0, 0), -1)
                    cv2.putText(frame, "Open Hand", (0, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                else:
                    hand_status = "Closed"
                    cv2.rectangle(frame, (0, 0), (200, 60), (255, 0, 0), -1)
                    cv2.putText(frame, "Closed Hand", (0, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                
                

        # Display the frame
        cv2.imshow("Hand Detection", frame)
        # Check for the 'q' key to exit
        if cv2.waitKey(1) == ord("q"):
            break

        

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()