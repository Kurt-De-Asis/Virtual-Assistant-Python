import pyttsx3
import speech_recognition
import datetime
import os
import wikipedia
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source,timeout=15,phrase_time_limit=30)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Sebastian. how can I help you today master?")

def sendEmail(to,content):
    server = smtplib.SMTP('mtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendemail('your email id', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    # while True:
    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            apath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(apath)

        elif "open adobe" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd31.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "wikipedia" in query:
            speak("searching in wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open_new(f"{cm}")

        elif 'play' in query:
            query = query.replace('play', '')
            speak('playing ' + query)
            pywhatkit.playonyt(query)

        elif "send email" in query:
            try:
                speak("what would you like me to say?")
                content = takecommand().lower()
                to = "kurtrussel644@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent " + to)

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email to " + to)

        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com")

        elif "open classroom" in query:
            webbrowser.open("https://classroom.google.com/u/1/h")

        elif "open pd101" in query:
            webbrowser.open("https://classroom.google.com/u/1/c/NTQ0NzU5NDcxMzQw")

        elif "open math" in query:
            webbrowser.open("https://classroom.google.com/u/1/c/NTM5MzI2MTQxMzEx")

        elif "join meeting" in query:
            webbrowser.open("https://meet.google.com/czj-hbsi-ywc")


        elif "no thanks" in query:
            speak("thanks for using me sir, have a nice day")
            sys.exit()

        speak("study well master kurt")
