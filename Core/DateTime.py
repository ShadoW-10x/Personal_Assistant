import datetime


def Date():
    return "The date is " + datetime.date.today().strftime("%B %d %Y")
def Time():
    return "The time is " + datetime.datetime.now().strftime("%H hours and %M minutes")