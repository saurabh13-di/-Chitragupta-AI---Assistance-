import threading
import tkinter as tk
from tkinter import scrolledtext
from assistant.commands import get_response,get_due_reminders
from assistant.voice import VoiceService
class ChitraguptaApp(tk.Tk):
    def __init__(self):
        super().__init__(); self.title('Chitragupta - Personal Virtual Assistant'); self.geometry('900x700'); self.minsize(680,520); self.configure(bg='#101827'); self.voice=VoiceService(); self._build_ui(); self._add_message('Chitragupta',"Hello! I am Chitragupta. Type a command or press Speak. Type 'help' for commands."); self.after(1000,self._check_reminders)
    def _build_ui(self):
        h=tk.Frame(self,bg='#17243a',padx=20,pady=14); h.pack(fill='x')
        tk.Label(h,text='CHITRAGUPTA',font=('Segoe UI',23,'bold'),fg='white',bg='#17243a').pack(anchor='w')
        tk.Label(h,text='Your Personal Voice & Text Assistant',font=('Segoe UI',10),fg='#9fb3cc',bg='#17243a').pack(anchor='w')
        self.chat=scrolledtext.ScrolledText(self,wrap=tk.WORD,state='disabled',font=('Segoe UI',10),bg='#f4f7fb',fg='#172033',padx=14,pady=14,relief='flat'); self.chat.pack(fill='both',expand=True,padx=18,pady=(16,10)); self.chat.tag_config('user',foreground='#1459a6',font=('Segoe UI',10,'bold')); self.chat.tag_config('chitragupta',foreground='#087f5b',font=('Segoe UI',10,'bold')); self.chat.tag_config('body',foreground='#172033')
        f=tk.Frame(self,bg='#101827',padx=18,pady=10); f.pack(fill='x'); self.entry=tk.Entry(f,font=('Segoe UI',12),relief='flat'); self.entry.pack(side='left',fill='x',expand=True,ipady=11,padx=(0,8)); self.entry.bind('<Return>',lambda e:self.send_text())
        tk.Button(f,text='Send',command=self.send_text,bg='#2563eb',fg='white',relief='flat',padx=18,pady=10).pack(side='left',padx=3); self.speak_button=tk.Button(f,text='🎙 Speak',command=self.start_listening,bg='#0f9d75',fg='white',relief='flat',padx=14,pady=10); self.speak_button.pack(side='left',padx=3)
        q=tk.Frame(self,bg='#101827',padx=18); q.pack(fill='x')
        for label,cmd in [('Help','help'),('Weather','weather in Delhi'),('System Info','system information'),('Show Notes','show notes')]: tk.Button(q,text=label,command=lambda c=cmd:self.process_user_text(c),bg='#26364f',fg='white',relief='flat',padx=10,pady=7).pack(side='left',padx=3)
        tk.Label(self,text='Chitragupta • Python Tkinter • Voice + Text',bg='#101827',fg='#9fb3cc',font=('Segoe UI',9)).pack(pady=8)
    def _add_message(self,sender,message):
        self.chat.configure(state='normal'); self.chat.insert(tk.END,f'{sender}: ','user' if sender=='You' else 'chitragupta'); self.chat.insert(tk.END,f'{message}\n\n','body'); self.chat.configure(state='disabled'); self.chat.see(tk.END)
    def send_text(self):
        text=self.entry.get().strip()
        if text: self.entry.delete(0,tk.END); self.process_user_text(text)
    def process_user_text(self,text):
        self._add_message('You',text); response,speak=get_response(text); self._add_message('Chitragupta',response)
        if speak: threading.Thread(target=self._speak_safely,args=(response,),daemon=True).start()
        if text.lower().strip() in ('exit','quit','goodbye','stop'): self.after(1800,self.destroy)
    def _speak_safely(self,text):
        try: self.voice.speak(text)
        except Exception as e: self.after(0,lambda:self._add_message('Chitragupta',f'Voice output unavailable: {e}'))
    def start_listening(self):
        self.speak_button.config(state='disabled',text='Listening...'); threading.Thread(target=self._listen_worker,daemon=True).start()
    def _listen_worker(self):
        try:
            text=self.voice.listen()
            if text: self.after(0,lambda:self.process_user_text(text))
            else: self.after(0,lambda:self._add_message('Chitragupta','Sorry, I could not understand. Try again.'))
        except Exception as e: self.after(0,lambda:self._add_message('Chitragupta',f'Microphone error: {e}'))
        finally: self.after(0,lambda:self.speak_button.config(state='normal',text='🎙 Speak'))
    def _check_reminders(self):
        try:
            for item in get_due_reminders():
                msg='Reminder: '+item['message']; self._add_message('Chitragupta',msg); threading.Thread(target=self._speak_safely,args=(msg,),daemon=True).start()
        except Exception as e: self._add_message('Chitragupta',f'Reminder error: {e}')
        self.after(1000,self._check_reminders)
