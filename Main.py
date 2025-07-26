from Util.Listen import command
from Util.Voice import Speak
from Core.command_router import command_map

# query = command()
query = "hello"

for key , fun in command_map.items:
    if key in query:
        command_map[key]()
        
    
else: print("command not found")
        


