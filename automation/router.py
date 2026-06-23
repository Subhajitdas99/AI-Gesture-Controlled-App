from automation.actions import *


ACTIONS = {

    "hello": wake_assistant,

    "yes": confirm_action,

    "thanks": close_assistant,

    "rock": open_vscode,

    "one": open_youtube,

    "nice": open_github,
}


def execute(prediction):

    try:

        if prediction in ACTIONS:

            ACTIONS[prediction]()

        else:

            print(
                f"[INFO] No action mapped for "
                f"'{prediction}'"
            )

    except Exception as e:

        print(
            f"[ERROR] Action execution failed: "
            f"{e}"
        )