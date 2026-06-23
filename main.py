
import cv2
import time
import traceback

from gesture.predict import GestureRecognizer
from automation.router import execute


def main():

    print("=" * 60)
    print("🤖 GestureGPT Starting...")
    print("=" * 60)

    try:

        print("[STEP 1] Loading Gesture Recognizer...")

        recognizer = GestureRecognizer()

        print("[STEP 2] Gesture Recognizer Loaded")

    except Exception:

        print("[ERROR] Failed to load recognizer")
        traceback.print_exc()

        return

    try:

        print("[STEP 3] Opening Webcam...")

        cap = cv2.VideoCapture(
            0,
            cv2.CAP_DSHOW
        )

        print("[STEP 4] Webcam Object Created")

        if not cap.isOpened():

            print("[ERROR] Camera not found")

            return

        print("[OK] Webcam Opened")

    except Exception:

        print("[ERROR] Camera initialization failed")
        traceback.print_exc()

        return

    last_gesture = None

    gesture_start_time = 0

    COOLDOWN_SECONDS = 5

    print("[READY] GestureGPT Running")
    print("[INFO] Press Q to Quit")

    while True:

        try:

            ret, frame = cap.read()

            if not ret:

                print("[ERROR] Frame read failed")

                break

            frame = cv2.flip(
                frame,
                1
            )

            prediction, confidence = recognizer.predict(
                frame
            )

            if (
                prediction is not None
                and confidence > 0.85
            ):

                cv2.putText(
                    frame,
                    f"{prediction} ({confidence:.2f})",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                current_time = time.time()

                if prediction != last_gesture:

                    print(
                        f"[GESTURE] "
                        f"{prediction} "
                        f"({confidence:.2f})"
                    )

                    execute(prediction)

                    last_gesture = prediction

                    gesture_start_time = current_time

                elif (
                    current_time - gesture_start_time
                    > COOLDOWN_SECONDS
                ):

                    last_gesture = None

            else:

                last_gesture = None

            cv2.imshow(
                "GestureGPT",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                print("[EXIT] User Quit")

                break

        except KeyboardInterrupt:

            print("[EXIT] Keyboard Interrupt")

            break

        except Exception:

            print("[ERROR] Runtime Exception")

            traceback.print_exc()

            break

    print("[CLEANUP] Releasing Resources")

    cap.release()

    cv2.destroyAllWindows()

    print("[DONE] GestureGPT Closed")


if __name__ == "__main__":

    main()



