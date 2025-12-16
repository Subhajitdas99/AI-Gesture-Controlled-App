import webbrowser
import time
import subprocess
import os

last_open_time = {}
COOLDOWN = 4  # seconds


def open_vscode():
    try:
        subprocess.Popen(["code"])
        return
    except:
        pass

    vscode_path = os.path.expandvars(
        r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    )
    if os.path.exists(vscode_path):
        subprocess.Popen(vscode_path)


def open_spotify():
    try:
        subprocess.Popen(["spotify"])
    except:
        webbrowser.open("https://open.spotify.com")


def open_excel():
    try:
        subprocess.Popen(["excel"])
        return
    except:
        pass

    possible_paths = [
        r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            break


def open_website(gesture):   # 👈 THIS MUST EXIST AT TOP LEVEL
    now = time.time()
    last = last_open_time.get(gesture, 0)

    if now - last < COOLDOWN:
        return

    if gesture == "hello":
        open_vscode()

    elif gesture == "rock":
        open_spotify()

    elif gesture == "one":
        open_excel()

    elif gesture == "yes":
        webbrowser.open("https://www.youtube.com")

    elif gesture == "three":
        webbrowser.open("https://mail.google.com")

    elif gesture == "nice":
        webbrowser.open("https://github.com/Subhajitdas99")

    elif gesture == "thanks":
        webbrowser.open("https://www.linkedin.com/in/subhajit-das-8207ab240/")

    last_open_time[gesture] = now
