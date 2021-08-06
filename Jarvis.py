import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning AD ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon AD")
    else:
        speak("Good Evening AD ")
    speak("Naan   thaa     Jaarvis   , , Ongalukaga  Naa  enna pannalaam ")
    speak("The Time is ")
    time()




def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        o=r.listen(source)
    try:
        print("Wait for few moments")
        query=r.recognize_google(o,language="en-in")
        print("user said ", query)
    except Exception as e :
        print(e)
        speak("Say that Again Please ")











if __name__ == "__main__":
    wishme()
    takecommand()

    while True :
        wishme()
        query = takecommand().lower()

        if"wikipedia" in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia" ,"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            speak(results)
            print(results)

        elif"open youtube" in query:
            speak("opening Boss")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening Boss")
            webbrowser.open("google.com")

        elif "open code"in query:
            speak("opening Boss")
            codepath = "C:\\Users\\Murali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open chrome"in query:
            speak("opening Boss")
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
 
    


       
            
   
























