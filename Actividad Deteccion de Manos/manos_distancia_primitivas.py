import math

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    left_index = None
    right_index = None

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks, results.multi_handedness
        ):
            label = handedness.classification[0].label
            h, w, _ = frame.shape

            index_tip = hand_landmarks.landmark[8]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            if label == "Left":
                left_index = (x, y)
            elif label == "Right":
                right_index = (x, y)

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if left_index and right_index:
            # Dibujar línea y círculos
            cv2.line(frame, left_index, right_index, (0, 255, 0), 3)
            cv2.circle(frame, left_index, 8, (255, 0, 0), -1)
            cv2.circle(frame, right_index, 8, (0, 0, 255), -1)

            # Calcular distancia entre dedos
            dx = left_index[0] - right_index[0]
            dy = left_index[1] - right_index[1]
            distance = math.sqrt(dx**2 + dy**2)

            # Calcular punto medio
            mid_x = int((left_index[0] + right_index[0]) / 2)
            mid_y = int((left_index[1] + right_index[1]) / 2)

            # Escalar rectángulo según la distancia
            rect_size = int(distance * 0.3)  # Ajuste de escala
            half_size = rect_size // 2

            # Calcular esquinas del rectángulo
            top_left = (mid_x - half_size, mid_y - half_size)
            bottom_right = (mid_x + half_size, mid_y + half_size)

            # Dibujar rectángulo
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)

    cv2.imshow("Hand Distance Rectangle", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
