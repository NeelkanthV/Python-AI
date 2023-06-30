 # Martian personal AI Aassistant

from winreg import QueryValue
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import microphone
from webbrowser import open
import subprocess as sp


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Print(voices [0].id)
# For a male voice, type [0], and for a female voice, type[1]!
engine.setProperty('voice',voices[0].id) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening! I hope you had a lovely day and that,better yet,is coming tomorrow")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Sorry i could not understand could you please say that again')
        return "None"
    return query    

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        if 'name of your creator' in query:
            speak('Neelkanth')
        elif 'How far is Mars from Earth?' in query:
            speak('On average, Mars is 225 million kilometers away from Earth.')
        elif 'how are you' in query:
            speak('i am fine')
          
        # Let's tell Martian to print the entire code!
        elif 'program for speed dial button menu in kivy MD'in query or 'speed dial button menu using kiwi MD' in query or 'speed dial button in python' in query:
            print("""
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivymd.app import MDApp


class Example(MDApp):
    data = DictProperty
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.data = {
            'Python': 'language-python',
            'Java': [
                'language-java',
                "on_press", lambda x: print("pressed Java"),
                "on_release", lambda x: print(
                    "stack_buttons",
                    self.root.ids.speed_dial.stack_buttons)
],
'PHP': [
     'language-php',
     "on_press", lambda x: print("pressed PHP"),
     "on_release", self.callback
],
'C++': [
     'language-cpp',
     "on_press", lambda x: print("pressed C++"),
     "on_release", lambda x: self.callback()
],
}
        return Builder.load_string('''
MDScreen:
    MDFloatingActionButtonSpeedDial:
        id: speed_dial
        data: app.data
        root_button_anim: True
        hint_animation: True''')   

    def callback(self, *args):
        print(args)

Example().run()
""")
        
        elif "who are you" in query:
            speak("Sir I am Martian personal aasistant")
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...Please wait")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences = 2)
            speak("wikipedia says")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open('www.google.co.in')
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")
        elif 'oepn google maps' in query:
            webbrowser.open("https://www.google.com/maps/")
        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:',shell=True)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using martian sir")
            exit()
                   

