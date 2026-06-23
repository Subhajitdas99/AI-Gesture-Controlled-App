# collect.py
import cv2, csv, os, time
import mediapipe as mp
import numpy as np

LABEL = "hello"
  # change per run or accept CLI arg
OUT_DIR = "dataset_landmarks"
os.makedirs(OUT_DIR, exist_ok=True)
csv_path = os.path.join(OUT_DIR, f"{LABEL}.csv")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
print("Press SPACE to record a sample for label:", LABEL)
print("Press q to quit.")

with open(csv_path, "a", newline="") as f:
    writer = csv.writer(f)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.flip(frame, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        res = hands.process(img_rgb)
        h, w, _ = img.shape
        if res.multi_hand_landmarks:
            lm = res.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(img, lm, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Collect", img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        if k == 32:  # space = record
            if res.multi_hand_landmarks:
                lm = res.multi_hand_landmarks[0]
                coords = []
                # normalize relative to wrist (landmark 0)
                x0 = lm.landmark[0].x
                y0 = lm.landmark[0].y
                for p in lm.landmark:
                    coords.append(p.x - x0)
                    coords.append(p.y - y0)
                    coords.append(p.z)  # optional
                writer.writerow(coords)
                print("Saved sample", time.time())
            else:
                print("No hand detected — try again.")
cap.release()
cv2.destroyAllWindows()
