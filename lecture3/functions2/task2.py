from movies import movies

import random

def sublist():

    for i in movies:
        i = random.choice(movies)
        if i["imdb"] >= 5.5:
            print(i["name"])

sublist()