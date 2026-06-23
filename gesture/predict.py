import cv2
import json
import time
import numpy as np
import mediapipe as mp

from tensorflow.keras.models import load_model
from collections import deque, Counter


class GestureRecognizer:

    def __init__(self):

        self.model = load_model("models/sign_language_model.h5")

        with open("models/label_map.json") as f:
            self.label_map = json.load(f)

        self.label_map = {
            int(k): v for k, v in self.label_map.items()
        }

        self.prediction_buffer = deque(maxlen=8)

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

    def extract_landmarks(self, hand):

        x0 = hand.landmark[0].x
        y0 = hand.landmark[0].y

        data = []

        for p in hand.landmark:
            data.extend([
                p.x - x0,
                p.y - y0,
                p.z
            ])

        return np.array(data).reshape(1, -1)

    def predict(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        if not result.multi_hand_landmarks:
            return None, 0

        hand = result.multi_hand_landmarks[0]

        self.drawer.draw_landmarks(
            frame,
            hand,
            self.mp_hands.HAND_CONNECTIONS
        )

        data = self.extract_landmarks(hand)

        probs = self.model.predict(
            data,
            verbose=0
        )[0]

        idx = np.argmax(probs)

        confidence = probs[idx]

        self.prediction_buffer.append(
            self.label_map[idx]
        )

        prediction = Counter(
            self.prediction_buffer
        ).most_common(1)[0][0]

        return prediction, confidence