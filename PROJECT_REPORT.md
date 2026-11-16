# CHITRAGUPTA – PERSONAL VIRTUAL ASSISTANT

## Abstract
Chitragupta is a Python desktop virtual assistant supporting text and voice interaction. It integrates a Tkinter GUI, speech recognition, text-to-speech, command processing, weather lookup, reminders, calculator, notes and system information.

## Objectives
1. Build a desktop assistant using Python.
2. Accept text and voice input.
3. Convert speech to text and generate spoken responses.
4. Automate simple tasks using commands.
5. Demonstrate modular programming and Python library integration.

## Requirements
Python 3.10+, VS Code, Tkinter, SpeechRecognition, PyAudio, pyttsx3, requests, psutil, Wikipedia package, microphone, speakers and internet connection.

## Modules
- GUI: displays chat and controls using Tkinter.
- Voice: captures microphone audio and speaks responses.
- Commands: detects user commands and calls modules.
- Weather: retrieves current city weather from Open-Meteo.
- Reminder: stores reminders in JSON and checks due reminders.
- Calculator: safely evaluates arithmetic expressions.
- Notes: adds, displays and clears notes in JSON.
- System Information: displays OS, CPU, RAM, disk and battery where supported.

## Working
The user types a command or presses Speak. Speech is converted to text. The command processor identifies the request and invokes the relevant module. The response is displayed and selected responses are spoken. Notes and reminders are stored locally in JSON files.

## Algorithm
1. Start the application and initialize the GUI.
2. Accept text input or voice input.
3. Convert microphone audio to text when voice mode is used.
4. Pass input to the command processor.
5. Identify the command and invoke its module.
6. Execute the task and prepare a response.
7. Display and optionally speak the response.
8. Check reminders periodically while the application is running.
9. Repeat until the user exits.

## Limitations
Voice recognition and weather require internet. Microphone operation depends on PyAudio and device permissions. Commands are rule-based. Reminders notify only while the app is running. Some system metrics depend on hardware support.

## Future Scope
Generative AI integration, multilingual speech, recurring/background reminders, database storage and email/calendar integrations.

## Conclusion
Chitragupta demonstrates Python GUI programming, speech recognition, text-to-speech, web APIs, JSON storage and system utilities in a modular virtual assistant.
