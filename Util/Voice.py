import pyttsx3

engine = pyttsx3.init()

def Speak(voice):
    engine.say(voice)
    engine.runAndWait()