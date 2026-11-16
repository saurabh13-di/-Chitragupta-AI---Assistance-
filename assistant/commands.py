from datetime import datetime
import webbrowser,urllib.parse
from assistant.calculator import calculate
from assistant.notes import add_note,get_notes,clear_notes
from assistant.reminders import parse_and_add
from assistant.weather import get_weather
from assistant.system_info import get_system_info
try: import wikipedia
except ImportError: wikipedia=None

def get_response(user_text):
    text=user_text.strip(); q=text.lower()
    if not q: return 'Please type or say something.',False
    if q in ('help','commands','what can you do'):
        return ("Commands: hello; time; date; open google; open youtube; search google for <topic>; search youtube for <topic>; wikipedia <topic>; weather in <city>; calculate <expression>; remind me in 10 minutes to study; remind me at 18:30 to study; note add <text>; show notes; clear notes; system information; goodbye"),False
    if any(x in q for x in ('hello','hi','hey','namaste')): return 'Hello! I am Chitragupta. How can I help you?',True
    if 'your name' in q or 'who are you' in q: return 'I am Chitragupta, your Python-based personal virtual assistant.',True
    if 'time' in q: return f"The current time is {datetime.now().strftime('%I:%M %p')}.",True
    if 'date' in q or 'today' in q: return f"Today is {datetime.now().strftime('%A, %d %B %Y')}.",True
    if q=='open google': webbrowser.open('https://google.com'); return 'Opening Google.',True
    if q=='open youtube': webbrowser.open('https://youtube.com'); return 'Opening YouTube.',True
    if q=='open wikipedia': webbrowser.open('https://wikipedia.org'); return 'Opening Wikipedia.',True
    if q.startswith('search google for '):
        query=text[len('search google for '):].strip(); webbrowser.open('https://google.com/search?q='+urllib.parse.quote_plus(query)); return f'Searching Google for {query}.',True
    if q.startswith('search youtube for '):
        query=text[len('search youtube for '):].strip(); webbrowser.open('https://youtube.com/results?search_query='+urllib.parse.quote_plus(query)); return f'Searching YouTube for {query}.',True
    if q.startswith('weather in '):
        try: return get_weather(text[len('weather in '):].strip()),True
        except Exception as e: return f'Weather service error: {e}',False
    if q.startswith('calculate '):
        try: return f"Answer: {calculate(text[len('calculate '):])}",True
        except ValueError as e: return str(e),False
    if q.startswith('remind me '):
        try:
            due=parse_and_add(text); return f"Reminder saved for {due.strftime('%d %b at %I:%M %p')}. Keep Chitragupta running for the alert.",True
        except ValueError as e: return str(e),False
    if q.startswith('note add '):
        try: return f"Note saved. Total notes: {add_note(text[len('note add '):])}.",True
        except ValueError as e: return str(e),False
    if q in ('show notes','read notes','my notes'):
        notes=get_notes(); return ('No saved notes. Use: note add <your note>' if not notes else '\n'.join(f"{i+1}. {n['text']} ({n['created_at']})" for i,n in enumerate(notes))),False
    if q=='clear notes': clear_notes(); return 'All notes deleted.',True
    if q in ('system information','system info','computer information'): return get_system_info(),False
    if q.startswith('wikipedia '):
        if wikipedia is None: return 'Wikipedia package is not installed.',False
        try: return wikipedia.summary(text[len('wikipedia '):],sentences=2),True
        except Exception: return 'I could not find that Wikipedia topic.',True
    if q in ('goodbye','exit','quit','stop'): return 'Goodbye! Have a great day.',True
    return "I don't know that command yet. Type 'help' to see available commands.",True

def get_due_reminders():
    from assistant.reminders import due_reminders
    return due_reminders()
