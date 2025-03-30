import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Ruli")

MASTER = "ARUL"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning " + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
        if "Ruli" in query:
            query = query.replace("Ruli", "")
        return query

    except Exception as e:
        print(e)
        print("Say that again please...")
        return ""

speak("Hello, I am Ruli. I'm your assistant. May I help you?")
wishMe()

while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        except Exception as e:
            print(e)
            speak("Sorry, I could not find any information on Wikipedia.")

    elif "open youtube" in query:
        speak("Okay, opening YouTube. Get ready...")
        url = "https://www.youtube.com"
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        try:
            webbrowser.get(chrome_path).open(url)
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't open YouTube.")

    elif "play" in query.lower():
        speak("youtube opened...")
        song = query.replace("play", "")
        speak("playing" + song)
        print("playing" + song)
        pywhatkit.playonyt(song)


    elif "exit" in query:
        speak("Goodbye " + MASTER)
        break
