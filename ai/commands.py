from automation import actions
import webbrowser
import subprocess


def execute_voice_command(command):

    command = command.lower()

    print(f"[AI] Processing: {command}")

    if "youtube" in command:

        actions.open_youtube()

    elif "github" in command:

        actions.open_github()

    elif "gmail" in command:

        actions.open_gmail()

    elif "linkedin" in command:

        actions.open_linkedin()

    elif "whatsapp" in command:

        print("[ACTION] Opening WhatsApp Web")

        webbrowser.open(
            "https://web.whatsapp.com"
        )

    elif "chatgpt" in command:

        webbrowser.open(
            "https://chatgpt.com"
        )

    elif "google" in command:

        webbrowser.open(
            "https://google.com"
        )

    elif "vscode" in command or "vs code" in command:

        actions.open_vscode()

    elif "notepad" in command:

        actions.open_notepad()

    elif "calculator" in command:

        actions.open_calculator()

    elif "search" in command:

        query = command.replace(
            "search",
            ""
        ).strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    else:

        print(
            f"[AI] Unknown command: {command}"
        )