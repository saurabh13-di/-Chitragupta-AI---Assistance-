# Chitragupta – Personal Virtual Assistant
Python desktop assistant with Tkinter, text/voice interaction and command modules.

## Features
- Voice input (SpeechRecognition + PyAudio) and spoken output (pyttsx3)
- Text chat GUI, greetings, date/time, browser opening and web search
- Wikipedia summaries
- Weather by city via Open-Meteo (no API key)
- Reminder system saved in JSON
- Safe calculator (no eval)
- Notes manager (add/show/clear)
- System information (OS, CPU, RAM, disk, battery where supported)

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```
If activation is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and activate again.
If PyAudio fails, install a wheel compatible with your Python version. Text mode still works without a microphone.

## Commands
`hello`; `what is the time`; `what is the date`; `open google`; `open youtube`; `search google for <topic>`; `search youtube for <topic>`; `wikipedia Alan Turing`; `weather in Delhi`; `calculate 12 * (5 + 2)`; `remind me in 1 minute to check my assignment`; `remind me at 18:30 to revise DSA`; `note add Finish AI lab`; `show notes`; `clear notes`; `system information`; `help`; `goodbye`.

Weather and online speech recognition need internet. Reminders notify only while Chitragupta is running, although reminder data persists in `data/reminders.json`. This is an educational rule-based assistant, not a generative AI chatbot.
