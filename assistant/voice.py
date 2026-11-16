import threading

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


class VoiceService:
    def __init__(self):
        self._speak_lock = threading.Lock()

    def listen(self) -> str:
        if sr is None:
            raise RuntimeError("SpeechRecognition is not installed. Run pip install SpeechRecognition.")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            raise RuntimeError("Speech recognition service is unavailable. Check your internet connection.")

    def speak(self, text: str):
        if pyttsx3 is None:
            raise RuntimeError("pyttsx3 is not installed. Run pip install pyttsx3.")
        # A lock prevents two speech engines from speaking simultaneously.
        with self._speak_lock:
            engine = pyttsx3.init()
            engine.setProperty("rate", 175)
            engine.setProperty("volume", 1.0)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
