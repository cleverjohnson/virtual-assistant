import webbrowser
import pyttsx3   #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install SpeechRecognition
import pyaudio
import wikipedia
import time
#import pywhatkit                #library used to perform a google search
#import google
#import flask
from pywhatkit import search

engine = pyttsx3.init()
engine.setProperty("rate", 150)        #speed of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)    #different voices at index 0 1 and 2

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def Day():                  #day of the week
    day = datetime.datetime.today().weekday() + 1             #Days of the week have indexes starting at 0 for monday
    DaysOfTheWeek = DOW = {1: 'Monday', 2: 'Tuesday', 
     3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
      
    if day in DOW.keys():
        day_of_the_week = DOW[day]
        speak("The day is " + day_of_the_week)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(day)
    speak(month)
    speak(year)

def greetme():
    speak("Hi Clever!")
        
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("morning")
    elif hour >= 12 and hour < 18:
        speak("a good afternoon")
    elif hour >= 18 and hour <24:
        speak("good evening")
    else:
        speak("its past midnight!")
        
    speak("how can i be of service?")
    
def search():
    j = input.takecommand().lower
    speak("here are some results")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:     #input using the microphone
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Please Clever, i didnt get that, could you say it again please...")
        return "None"
    return query
    
def take_query():
    greetme()
    while(True):
        query = takeCommand().lower()
        if query == "open ilearn":
           speak("Opening Ilearn DIT")
           webbrowser.open("https://ilearn.th-deg.de/")
           
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
              
        elif "which day it is" in query:
            Day()
            continue
          
        elif "tell me the time" in query:
            time()
            continue
          
        elif "terminate" in query:                            #end my program
            speak("alrigh! am out of here")
            exit()
        
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
          
        elif "tell me your name" in query:
            speak("I am Clever's Assistant")
            
        #else:
        #    search()
take_query()
