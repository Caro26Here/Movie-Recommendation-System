from imdb import Cinemagoer
import numpy as np

# 1. Create a class called Movie with the following attributes: title, genre, rating, and year.
class movie:
    def __init__(self, title, genre, rating, year):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

    # 2. Implement methods in the Movie class to set and get the attributes.
    def set_movie(self):
        pass

    def get_movie(self):
        pass
        
movie1 = movie('Inception','Science Fiction',8.8,2010)
print('Movie:',movie1.title)
print('Genre:',movie1.genre)

# 3. Use a dictionary to store movie information, where the movie title is the key, 
# and the Movie object is the value.
new_movie = movie(input('Título de la película: '),input('Genero: '),input('Rating: '),input('Año de estreno: '))
movies_dict = {(movie.title): new_movie}

# 4. Implement a function to add movies to the system. The function should take movie 
# information as input and create a Movie object, storing it in the movie dictionary.
def add_movie(movies_dict):
    new_movie =  movie(input('Ingresa una peli: '),input('Ingresa el genero de la peli: '),input('Ingresa el rating de la peli: '),input('Ingresa el año de estreno de la peli: '))
    movies_dict.append(new_movie)

# 5. Implement a function to recommend movies to a user based on their preferred genre. The
# function should take a genre as input and return a list of movies with the highest ratings 
# in that genre.
add_movie()
movie_input = input('Ingresa el título de una película que te encante: ')

def movie_recommend(movie_input,movie_dict):
    movie_input


# 6. Use the NumPy package to calculate the average rating for movies in a given genre.

# 7. Implement a function to export the movie dictionary to a JSON file.

# 8. Implement a function to import movie information from a JSON file and update the movie 
# dictionary accordingly.

# 9. Write tests for all the implemented functions to ensure their correctness.

# 10. Use the math package to round the average ratings to two decimal places.