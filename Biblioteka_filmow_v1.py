
import random
from datetime import date  

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
         # Variables
        self.streams = 0

    def __str__(self):
        return f'{self.title} ({self.year}) {self.streams}\n'

    def play(self):
        self.streams +=1
        return f'{self.streams}'


class Serie(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d} {self.streams}\n'    
    
    def play(self):
        self.streams +=1
        return f'{self.streams}'


movie1 = Movie(title="Avatar", year = 2009, genre = "Sci-Fi")
movie2 = Movie(title="Avengers: Koniec gry", year = 2019, genre = "Sci-Fi")
movie3 = Movie(title="Titanic", year = 1997, genre = "Katastroficzny")
movie4 = Movie(title="Gwiezdne wojny: Przebudzenie Mocy", year = 2015, genre = "Przygodowy / Sci-Fi")
movie5 = Movie(title="Avengers: Wojna bez granic", year = 2018, genre = "Akcja / Sci-Fi")
movie6 = Movie(title="Spider-Man: Bez drogi do domu", year = 2021, genre = "Akcja / Sci-Fi")
movie7 = Movie(title="Jurassic World", year = 2015, genre = "Przygodowy / Sci-Fi")
movie8 = Movie(title="Król Lew", year = 2019, genre = "Animacja / Familijny / Przygodowy")
movie9 = Movie(title="Avengers", year = 2012, genre = "Akcja / Sci-Fi")
movie10 = Movie(title="Szybcy i wściekli 7", year = 2015, genre = "Akcja")
serie1 = Serie(title="Nasza planeta", year = 2019, genre = "Dokumentalny / Przyrodniczy", season = 1, episode = 1)
serie2 = Serie(title="Nasza planeta", year = 2019, genre = "Dokumentalny / Przyrodniczy", season = 1, episode = 2)
serie3 = Serie(title="Nasza planeta", year = 2019, genre = "Dokumentalny / Przyrodniczy", season = 1, episode = 3)
serie4 = Serie(title="Gra o tron", year = 2011, genre = "Dramat/Fantasy/Przygodowy", season = 1, episode = 9)
serie5 = Serie(title="Gra o tron", year = 2011, genre = "Dramat/Fantasy/Przygodowy", season = 1, episode = 10)
serie6 = Serie(title="Gra o tron", year = 2019, genre = "Dramat/Fantasy/Przygodowy", season = 8, episode = 5)
serie7 = Serie(title="Gra o tron", year = 2019, genre = "Dramat/Fantasy/Przygodowy", season = 8, episode = 6)

one_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, serie1, serie2, serie3, serie4, serie5, serie6, serie7]

filtered_list = []


def get_movies():
    for i in one_list:
        if isinstance(i,Serie)!= True:
            filtered_list.append(i)
        else:
            pass
    by_title_asc = sorted(filtered_list, key=lambda m: m.title)
    return by_title_asc

#get_movies()


def get_series():
    for i in one_list:
        if isinstance(i,Serie)== True:
            filtered_list.append(i)
        else:
            pass
    by_title_asc = sorted(filtered_list, key=lambda m: m.title)
    return by_title_asc

#get_series()

def search(title):    
    searched =[]
    for i in one_list:
        if title == i.title:
            searched.append(i)
            return i
        else:
            pass
    if len(searched)==0:
            print('Nie ma takiego tytułu w bibliotece!')

#search("Avataroo")

def generate_views():
    i = random.choice(one_list)
    i.streams = random.choice(range(1,101))
    return i


def run_generate_views():
    for i in range(10):
        generate_views()

#run_generate_views()


def top_titles(top_number, content_type):
  
    for i in one_list:
        i.streams = random.choice(range(1,101))
    if content_type == "Movie":
        get_movies()
    elif content_type == "Serie":
        get_series()
    else:
        print('Wybierz Movie albo Serie!')
        exit(1)


    by_popularity = sorted(filtered_list, key=lambda i: i.streams, reverse = True)
    today = date.today().strftime("%d.%m.%Y")
    tekst = f'Najpopularniejsze filmy i seriale dnia {today}:\n'

    return tekst,*by_popularity[0:top_number]


def main():
    result = "Biblioteka filmów\n"
    result2 = top_titles(3, "Movie")
    print(result, *result2)

if __name__ == "__main__":
    main()