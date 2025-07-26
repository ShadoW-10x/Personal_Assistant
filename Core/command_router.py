from .DateTime import Date , Time
from .Greet import Greet
from .News import News
from .Open_Apps import open
from ..Util.Voice import Speak
from .Weather import Weather
from .Wikipedia_search import SearchWikipedia
from ..Main import query

command_map = {
                "hello" : Speak(Greet) ,
                "on wikipedia" : Speak(SearchWikipedia(query)) , 
                "news" : News ,
                "date" : Speak(Date) ,
                "time" : Speak(Time) ,
                "weather" : Weather ,
                "temperature" : Weather ,
                "exit" : Speak("Good bye") ,
                "open" : open(query)


}

