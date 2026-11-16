import json
from pathlib import Path
from datetime import datetime
FILE=Path(__file__).resolve().parent.parent/'data'/'notes.json'
def _load():
    FILE.parent.mkdir(exist_ok=True)
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else []
    except (json.JSONDecodeError,OSError): return []
def add_note(text):
    if not text.strip(): raise ValueError('Note cannot be empty.')
    notes=_load(); notes.append({'text':text.strip(),'created_at':datetime.now().strftime('%d-%m-%Y %I:%M %p')})
    FILE.write_text(json.dumps(notes,indent=2,ensure_ascii=False),encoding='utf-8'); return len(notes)
def get_notes(): return _load()
def clear_notes(): FILE.write_text('[]',encoding='utf-8')
