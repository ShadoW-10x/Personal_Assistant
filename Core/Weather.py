import requests
import geocoder
import langdetect
from Util.Voice import Speak
from API_Keys import weather_api



def Weather(weather_api):
    location = geocoder.ip('me')
    loc = location.latlng
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api}&q={loc[0]},{loc[1]}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        Speak("The current weather is as follows \n" \
        f"the current temperature is {data['current']['temp_c']} degree celcius")
        Speak(f"with wind speed of {data['current']['wind_kph']} kilometer per hour")
        Speak(f"and the condition is {data['current']['condition']['text']}")