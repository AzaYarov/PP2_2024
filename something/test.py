from movies import movies

def sublist(films):
    sub = [i for i in movies if i["imdb"] >= 5.5]
    return sub

print(sublist(movies))