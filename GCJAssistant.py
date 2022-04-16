import pyttsx3   #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install SpeechRecognition
import pyaudio


engine =pyttsx3.init()
engine.setProperty("rate", 150)        #speed of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)    #different voices at index 0 1 and 2

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(day)
    speak(month)
    speak(year)

def greetme():
    speak("Welcome back Clever.")
    speak("The time is")
    time()
    speak("the current date is")
    date()
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("GOOD MORNING Clever")
    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON Clever")
    elif hour >= 18 and hour <24:
        speak("GOOD EVENING Clever")
    else:
        speak("HAVE A BLESSED NIGHT!")
        
    speak("so how can i help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:     #input using the microphone
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(query)
    except Exception as e:
        print(e)
        speak("Please Clever, i didnt get that, could you say it again please...")
        return "None"
    return query
