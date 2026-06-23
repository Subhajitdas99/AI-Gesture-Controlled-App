import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("[VOICE] Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        text = recognizer.recognize_google(audio)

        text = text.lower()

        print(
            f"[VOICE] You said: {text}"
        )

        return text

    except sr.UnknownValueError:

        print(
            "[VOICE] Could not understand audio"
        )

        return ""

    except sr.RequestError:

        print(
            "[VOICE] Speech service unavailable"
        )

        return ""

    except Exception as e:

        print(
            f"[VOICE ERROR] {e}"
        )

        return ""