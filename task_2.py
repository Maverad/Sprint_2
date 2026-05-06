class Movies():
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies

class Comedy(Movies):
    def __init__(self):
        super().__init__()
        self.comedies = set()

    def add_movie(self, movie):
        super().add_movie(movie)
        self.comedies.add(movie)
        return f'Комедии: {list(self.comedies)}'
    
class Drama(Movies):
    def __init__(self):
        super().__init__()
        self.dramas = set()

    def add_movie(self, movie):
        super().add_movie(movie)
        self.dramas.add(movie)
        return f'Драмы: {list(self.dramas)}'
    
comedy = Comedy()
drama = Drama()
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))