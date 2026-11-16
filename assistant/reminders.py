import json,re
from pathlib import Path
from datetime import datetime,timedelta
FILE=Path(__file__).resolve().parent.parent/'data'/'reminders.json'
def _load():
    FILE.parent.mkdir(exist_ok=True)
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else []
    except (json.JSONDecodeError,OSError): return []
def _save(items):
    FILE.parent.mkdir(exist_ok=True); FILE.write_text(json.dumps(items,indent=2,ensure_ascii=False),encoding='utf-8')
def parse_and_add(text):
    rest=text.strip()[len('remind me '):].strip(); now=datetime.now()
    m=re.match(r'in\s+(\d+)\s+(minute|minutes|min|hour|hours|hr|hrs)\s+to\s+(.+)$',rest,re.I)
    if m:
        amount,unit,message=int(m.group(1)),m.group(2).lower(),m.group(3).strip()
        if not 1<=amount<=10080: raise ValueError('Duration must be between 1 and 10080.')
        due=now+(timedelta(minutes=amount) if unit in ('minute','minutes','min') else timedelta(hours=amount))
    else:
        m=re.match(r'at\s+(\d{1,2}):(\d{2})\s+to\s+(.+)$',rest,re.I)
        if not m: raise ValueError('Use: remind me in 10 minutes to study OR remind me at 18:30 to study')
        h,minute,message=int(m.group(1)),int(m.group(2)),m.group(3).strip()
        if h>23 or minute>59: raise ValueError('Use 24-hour time, e.g. 18:30.')
        due=now.replace(hour=h,minute=minute,second=0,microsecond=0)
        if due<=now: due+=timedelta(days=1)
    if not message: raise ValueError('Enter a reminder message.')
    items=_load(); items.append({'message':message,'due_at':due.isoformat(timespec='seconds')}); _save(items); return due
def due_reminders():
    now=datetime.now(); due=[]; pending=[]
    for item in _load():
        try:
            (due if datetime.fromisoformat(item['due_at'])<=now else pending).append(item)
        except (KeyError,ValueError): pass
    _save(pending); return due
