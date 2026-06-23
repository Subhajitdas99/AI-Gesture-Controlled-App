import webbrowser
import subprocess
import os


def wake_assistant():

    print("\n🤖 GestureGPT Activated")

    print(
        "[AI] Waiting for voice command..."
    )

    try:

        from voice.listener import listen
        from ai.commands import execute_voice_command

        command = listen()

        if command:

            execute_voice_command(command)

        else:

            print(
                "[AI] No command detected"
            )

    except Exception as e:

        print(
            f"[AI ERROR] {e}"
        )


def confirm_action():

    print("[AI] Confirmed")


def close_assistant():

    print("[AI] Goodbye")


def open_youtube():

    print("[ACTION] Opening YouTube...")

    webbrowser.open(
        "https://youtube.com"
    )


def open_github():

    print("[ACTION] Opening GitHub...")

    webbrowser.open(
        "https://github.com"
    )


def open_gmail():

    print("[ACTION] Opening Gmail...")

    webbrowser.open(
        "https://mail.google.com"
    )


def open_linkedin():

    print("[ACTION] Opening LinkedIn...")

    webbrowser.open(
        "https://linkedin.com"
    )


def open_vscode():

    vscode_paths = [

        r"C:\Users\subha\AppData\Local\Programs\Microsoft VS Code\Code.exe",

        r"C:\Program Files\Microsoft VS Code\Code.exe",

        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe"
    ]

    for path in vscode_paths:

        if os.path.exists(path):

            subprocess.Popen([path])

            print(
                "[ACTION] VS Code Opened"
            )

            return

    print(
        "[ERROR] VS Code not found"
    )


def open_notepad():

    subprocess.Popen(
        ["notepad.exe"]
    )

    print(
        "[ACTION] Notepad Opened"
    )


def open_calculator():

    subprocess.Popen(
        ["calc.exe"]
    )

    print(
        "[ACTION] Calculator Opened"
    )