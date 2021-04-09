import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

# For static images:
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5)

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)

# For static images:
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    min_detection_confidence=0.5)
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# For webcam input:
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_mesh.process(image)
    results2 = hands.process(image)
    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mask = np.zeros(image.shape[:], dtype='uint8')
    if results.multi_face_landmarks:
      for handLms in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image=mask,
            landmark_list=handLms,
            connections=mp_face_mesh.FACE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)
        for id, lm in enumerate(handLms.landmark):
            # print(id,lm)
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            if id == 4:
                cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                print(id, cx, cy)

    if results2.multi_hand_landmarks:
      for hand_landmarks in results2.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            mask, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('MediaPipe FaceMesh', mask)
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
cap = cv2.VideoCapture(0)
face_mesh.close()
cap.release()
cv2.destroyAllWindows()