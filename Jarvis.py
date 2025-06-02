import speech_recognition as sr
import pyttsx3
import datetime 
import wikipedia as wp
from wikipedia.exceptions import PageError,DisambiguationError
import webbrowser as wb
import requests
import langdetect
import os


engine = pyttsx3.init()

def Speak(voice):
    engine.say(voice)
    engine.runAndWait()


def command():
    temp = sr.Recognizer()
    while True:
        with sr.Microphone() as voice:
            print("Listening.....")
            audio = temp.listen(voice)

        try:
            text = temp.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            Speak("Please repeat that again")
           



def Date():
    return "The date is " + datetime.date.today().strftime("%B %d %Y")
def Time():
    return "The time is " + datetime.datetime.now().strftime("%H hours and %M minutes")
  

def Greet(name = "Sanskar"):
    t = datetime.datetime.now().strftime("%H")
    t = int(t)
    if(t > 6 and t < 12): return f"Good Morning {name}, Have a wonderful day ahead"
    elif(t >= 12 and t <17): return f"Good Afternoon {name}, Hope You are good"
    elif(t >= 17 and t <= 21): return f"Good evening {name}"
    else: return f"You are up pretty late {name}, "

    
def SearchWikipedia(query):
    print("Searching....")
    pages = wp.search(query)

    for result in pages:
        try:
            return "According to Wikipedia , " + wp.summary(result , sentences = 3 )
            
        except DisambiguationError:
            continue

        except PageError:
            continue


def OpenApps(query):
    if "youtube" in query:
        Speak("Opening")
        wb.open("https://www.youtube.com/")

    elif "chatgpt" in query:
        Speak("Opening")
        wb.open("https://chatgpt.com/")

    elif "reddit" in query:
        Speak("Opening")
        wb.open("https://www.reddit.com/")

    elif "monkey type" in query:
        Speak("Opening")
        wb.open("https://monkeytype.com/")


    elif "browser" in query:
        Speak("Opening")
        os.startfile(r"C:\\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

    elif "spotify" in query:
        Speak("Opening")
        os.startfile(r"C:\Users\sansk\AppData\Roaming\Spotify\Spotify.exe")

    elif "vs code" in query:
        Speak("Opening")
        os.startfile(r"C:\Users\sansk\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    else:
        Speak("Command not valid")
        
    




def News(api = "pub_c831d8caad554c61bb14a241bab4941d"):
    url = f"https://newsdata.io/api/1/latest?apikey={api}&country=in"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        Speak("The top Headlines are ")
        for number,headline in enumerate(data['results'],start = 1):
            try:
                if(headline['description'] and langdetect.detect(headline['description']) == 'en'):
                    Speak(headline['description'])
                    print('\n')
            except TypeError:
                continue

            if number == 20: break
    
    else: print(response.status_code)




def main():

    
        Speak("Hello How may i assist you today")
        while True:
            query = command().lower()
            print(query)

            if "hello" in query: 
                Speak(Greet()) 
                
            elif "on wikipedia" in query: Speak(SearchWikipedia(query))

            elif "open" in query: OpenApps(query)

            elif "news" in query: News()

            elif "date" in query: Speak(Date())
            
            elif "time" in query: Speak(Time())

            elif "exit" in query or "quit" in query :
                Speak("Good bye")
                exit()

       
            


def trigger():
    Speak("im on standby")
    print("Hey")
    comm = command().lower()
    if 'jarvis' in comm:
        main()
    elif 'exit' in comm or 'quit' in comm: exit()
        


while True:
    trigger()

