import os
import webbrowser as wb
from Util.Voice import Speak

app_map = {

            "youtube" : lambda : wb.open("https://www.youtube.com/") , 
            "chatgpt" : lambda :wb.open("https://chatgpt.com/") ,
            "reddit" : lambda : wb.open("https://www.reddit.com/") ,
            "monkey type" : lambda : wb.open("https://monkeytype.com/") ,
            "browser" : lambda :  os.startfile(r"C:\\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe") ,
            "vs code" : lambda : os.startfile(r"C:\Users\sansk\AppData\Local\Programs\Microsoft VS Code\Code.exe") ,
            "spotify" : lambda :  os.startfile(r"C:\Users\sansk\AppData\Roaming\Spotify\Spotify.exe")
           
           }





def open(query):
    for key in app_map:
        if key in query:
            app_map[key]()
            return
    
    print("App not found")


