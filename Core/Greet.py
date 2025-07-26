import datetime

def Greet(name = "Sanskar"):
    t = datetime.datetime.now().strftime("%H")
    t = int(t)
    if(t > 6 and t < 12): return f"Good Morning {name}, Have a wonderful day ahead"
    elif(t >= 12 and t <17): return f"Good Afternoon {name}, Hope You are good"
    elif(t >= 17 and t <= 21): return f"Good evening {name}"
    else: return f"You are up pretty late {name}, "
