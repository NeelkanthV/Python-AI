
from cgitb import text
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# For a male voice, type [0], and for a female voice, type[1]!
engine.setProperty('voice',voices[0].id)
text = "Somewhere,something incredible is waiting to be known!"
engine.say(text)
engine.runAndWait()
