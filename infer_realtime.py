import cv2
import json
import time
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from collections import deque, Counter

from web_actions import open_website


# =========================
# Load model & labels
# =========================
model = load_model("sign_language_model.h5")

with open("label_map.json") as f:
    label_map = json.load(f)
label_map = {int(k): v for k, v in label_map.items()}


# =========================
# MediaPipe setup
# =========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils


# =========================
# Webcam + buffers
# =========================
cap = cv2.VideoCapture(0)
prediction_buffer = deque(maxlen=8)

last_triggered_gesture = None   # 🔑 KEY FIX
last_trigger_time = 0
TRIGGER_DELAY = 1.5             # seconds


# =========================
# Landmark extraction
# =========================
def extract_landmarks(hand):
    x0, y0 = hand.landmark[0].x, hand.landmark[0].y
    data = []
    for p in hand.landmark:
        data.extend([p.x - x0, p.y - y0, p.z])
    return np.array(data).reshape(1, -1)


# =========================
# Main loop
# =========================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # Predict
        data = extract_landmarks(hand)
        probs = model.predict(data, verbose=0)[0]
        idx = np.argmax(probs)
        confidence = probs[idx]

        prediction_buffer.append(label_map[idx])
        prediction = Counter(prediction_buffer).most_common(1)[0][0]

        if confidence > 0.85:
            cv2.putText(
                frame,
                f"{prediction} ({confidence:.2f})",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            now = time.time()

            # ✅ EDGE TRIGGER (ONLY ON CHANGE)
            if (
                prediction != last_triggered_gesture
                and now - last_trigger_time > TRIGGER_DELAY
            ):
                open_website(prediction)
                last_triggered_gesture = prediction
                last_trigger_time = now

    else:
        # Reset when no hand is detected
        last_triggered_gesture = None

    cv2.imshow("AI Gesture Controlled App Launcher", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# =========================
# Cleanup
# =========================
cap.release()
cv2.destroyAllWindows()
