import speech_recognition as sr
from Util.Voice import Speak


def command():
    temp = sr.Recognizer()
    while True:
        with sr.Microphone() as voice:
            print("Listening.....")
            audio = temp.listen(voice)

        try:
            text = temp.recognize_google(audio).lower()
            return text

        except sr.UnknownValueError:
            Speak("Please repeat that again")