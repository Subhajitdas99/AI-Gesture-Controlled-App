# 🤖 GestureGPT

### AI-Powered Multimodal Human-Computer Interaction System

GestureGPT is an intelligent Human-Computer Interaction (HCI) system that combines **Computer Vision**, **Deep Learning**, **Speech Recognition**, and **Desktop Automation** to enable touchless interaction with a computer using hand gestures and voice commands.

Users can activate the AI assistant using a predefined hand gesture and then interact through natural voice commands to launch applications, open websites, search the web, and control desktop actions.

---

# 🚀 Features

## 🖐️ Gesture Recognition

* Real-time hand tracking using MediaPipe
* Deep learning-based gesture classification
* Custom gesture dataset training
* Gesture smoothing using prediction buffers
* Confidence-based filtering

Supported Gestures:

| Gesture | Action                |
| ------- | --------------------- |
| hello   | Activate AI Assistant |
| yes     | Confirm Action        |
| thanks  | Close Assistant       |
| one     | Open YouTube          |
| nice    | Open GitHub           |
| rock    | Open VS Code          |

---

## 🎤 Voice Assistant

After detecting the wake gesture:

```text
hello
```

GestureGPT enters voice mode.

Example commands:

```text
open youtube
open github
open gmail
open linkedin
open vscode
open notepad
open calculator
search ai internship in kolkata
```

---

## 🌐 Browser Automation

GestureGPT can automatically open:

* YouTube
* GitHub
* Gmail
* LinkedIn
* Google Search
* WhatsApp Web

---

## 💻 Desktop Automation

GestureGPT can launch:

* Visual Studio Code
* Notepad
* Calculator

Additional applications can be added easily.

---

## 🧠 AI Assistant Mode

Workflow:

```text
Gesture
    ↓
Voice Command
    ↓
Intent Recognition
    ↓
Action Execution
```

Example:

```text
👋 hello

🎤 search ai internship in kolkata

🌐 Opens Google Search
```

---

# 🏗️ System Architecture

```text
Webcam
   ↓
MediaPipe Hand Tracking
   ↓
TensorFlow Gesture Model
   ↓
Gesture Recognition
   ↓
Action Router
   ↓
Voice Recognition
   ↓
Command Processing
   ↓
Desktop / Browser Automation
```

---

# 📂 Project Structure

```text
GestureGPT/

├── ai/
│   └── commands.py
│
├── automation/
│   ├── actions.py
│   └── router.py
│
├── gesture/
│   ├── collect.py
│   ├── train_landmarks.py
│   ├── predict.py
│   └── infer_realtime.py
│
├── voice/
│   └── listener.py
│
├── models/
│   ├── sign_language_model.h5
│   └── label_map.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

## Computer Vision

* OpenCV
* MediaPipe

## Deep Learning

* TensorFlow
* Keras

## Machine Learning

* NumPy
* Scikit-Learn

## Speech Recognition

* SpeechRecognition
* PyAudio

## Automation

* WebBrowser
* Subprocess

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Subhajitdas99/AI-Gesture-Controlled-App.git

cd AI-Gesture-Controlled-App
```

Create virtual environment:

```bash
python -m venv venv

venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run GestureGPT

```bash
python main.py
```

Output:

```text
🤖 GestureGPT Starting...

[OK] Webcam Opened

[READY] GestureGPT Running
```

Quit:

```text
Press Q
```

---

# 📊 Current Capabilities

✅ Real-time Gesture Recognition

✅ Voice Command Recognition

✅ Website Automation

✅ Desktop Automation

✅ AI Assistant Activation

✅ Gesture-to-Voice Interaction

---

# 🔮 Future Scope

Planned GestureGPT v3 Features:

* Ollama Integration
* Local LLM Support
* Memory System
* Conversational AI
* Agentic Tool Calling
* File Management
* Email Automation
* Smart Desktop Assistant

Future Workflow:

```text
Gesture
    ↓
Voice
    ↓
LLM
    ↓
Reasoning
    ↓
Tool Selection
    ↓
Action Execution
```

---

# 🎓 Academic Relevance

This project demonstrates:

* Human Computer Interaction (HCI)
* Computer Vision
* Deep Learning
* Speech Recognition
* AI Automation
* Real-Time Systems

Suitable for:

* Final Year Engineering Project
* AI & ML Project Portfolio
* Research Prototype
* Smart Accessibility Systems

---

# 👨‍💻 Author

**Subhajit Das**

B.Tech CSE (AI & ML)

Dr. Sudhir Chandra Sur Institute of Technology & Sports Complex

West Bengal, India

GitHub:
https://github.com/Subhajitdas99

