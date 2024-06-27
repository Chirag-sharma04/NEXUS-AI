import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newsapi="Your-news-api"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hy! I am Nexus Virtual Assistant Please tell how may I help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said {query} \n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()
def sendEmail(to,subject,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #Identify ourselves to the SMTP server
    server.starttls() #Secure the SMTP connection
    server.login('your-email@gmail.com','app-password')
    server.sendmail('reciever-email',to,subject,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query=takecommand()
        if 'about' in query:
            speak("Searching Wikipedia ...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open wikipedia' in query:
            webbrowser.open('wikipedia.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime}")
        elif 'open code' in query:
            codepath="path-vs-code"
            os.startfile(codepath)
        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takecommand()
                subject="Email through python"
                to="reciever-email"
                sendEmail(to,subject,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend.I am not able to send this email.")
        elif 'thank you' in query:
            speak("It's my pleasure to help you")
        elif 'open python' in query:
            codepath="path//"
            os.startfile(codepath)
        elif 'open notepad' in query:
            codepath="Path//"
            os.startfile(codepath)
        elif 'play music' in query:
            music_dir="path//"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'quit' in query:
            speak("Okay,Have a good day ahead! BYE")
            exit()
        elif 'news' in query:
            r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code==200:
                data=r.json()
                articles=data.get('articles',[])
                for article in articles:
                    speak(article['title'])
                    print(article['title'])
        else:
            speak("Error in finding......")

