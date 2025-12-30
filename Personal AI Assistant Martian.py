"""
Martian AI Assistant - CSV-Driven
Description:
    A voice-controlled assistant that reads commands and responses from a CSV dataset.
    Users speak commands, and Martian replies or performs actions like opening websites.
    This approach demonstrates how to use structured data in Python projects.

Note:
    You can create your own CSV file named 'martian_dataset.csv' inside a 'data' folder.
    It should have two columns: 'command' and 'response'.
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pandas as pd
import os

# Constants 
DATA_FILE = "data/martian_dataset.csv"

# Load Dataset 
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    # If the CSV doesn't exist, we'll create a default dataset.
    # You can modify this or create your own CSV later.
    data = {
        "command": [
            "name of your creator",
            "how far is mars from earth",
            "how are you",
            "who are you",
            "open youtube",
            "open google",
            "open google maps",
            "open whatsapp",
            "the time",
            "wikipedia python"
        ],
        "response": [
            "Neelkanth",
            "On average, Mars is 225 million kilometers away from Earth.",
            "I am fine",
            "I am Martian, your personal assistant.",
            "Opening YouTube",
            "Opening Google",
            "Opening Google Maps",
            "Opening WhatsApp",
            "[Current Time]",
            "[Wikipedia Summary]"
        ]
    }
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(DATA_FILE, index=False)

# Text-to-Speech Setup 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Speak the given text aloud."""
    engine.say(text)
    engine.runAndWait()

# Greetings
def wish_me():
    """Greet the user based on current time."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning Sir!")
    elif hour < 17:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening! Have a great day!")

# Listen for Voice Input
def take_command():
    """Listen to the user's voice and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        print("Could not understand audio. Please repeat.")
        return "none"
    return query.lower()

#Get Response from CSV 
def get_response(query):
    """Check the CSV dataset for a matching command and respond."""
    row = df[df['command'].str.lower() == query.lower()]
    if not row.empty:
        response = row['response'].values[0]

        # Handle dynamic responses
        if response == "[Current Time]":
            response = datetime.datetime.now().strftime("%H:%M:%S")
        elif response == "[Wikipedia Summary]":
            try:
                topic = query.replace("wikipedia", "").strip()
                response = wikipedia.summary(topic, sentences=2)
            except:
                response = "No results found on Wikipedia."

        # Open websites if applicable
        if "open youtube" in query:
            webbrowser.open("https://youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "open google maps" in query:
            webbrowser.open("https://www.google.com/maps/")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")

        return response
    elif query in ["quit", "exit", "close"]:
        return "exit"
    else:
        return None

# Main Program
if __name__ == "__main__":
    wish_me()
    speak("I am Martian, your CSV-driven assistant. How can I help you today?")

    while True:
        query = take_command()
        if query == "none":
            continue

        response = get_response(query)
        if response == "exit":
            speak("Thank you for using Martian. Goodbye!")
            break
        elif response is None:
            speak("I don't know this command yet. Try another one.")
        else:
            speak(response)


