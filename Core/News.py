import requests
from Util.Voice import Speak
import langdetect
from API_Keys import news_api


def News(news_api):
    url = f"https://newsdata.io/api/1/latest?apikey={news_api}&country=in"
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
