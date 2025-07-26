import wikipedia as wp
from wikipedia.exceptions import PageError,DisambiguationError


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