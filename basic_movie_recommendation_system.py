import numpy as np
import json

class MovieEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Movie):
            movie_dict = {
                obj.title : [obj.title, obj.genre, obj.rating, obj.year]
            }
            return movie_dict
        return super().default(obj)
    

class Movie:
    def __init__(self, title, genre, rating, year):
        self.title = str(title)
        self.genre = str(genre)
        self.rating = float(rating)
        self.year = int(year)

# 8. Implement a function to import movie information from a JSON file and update the movie 
# dictionary accordingly.
def import_dict():
    with open('movies.json', 'r') as json_file:
        movies_dict = json.load(json_file)

    return movies_dict


def valid_genre(new_movie):
    genre = new_movie.genre.lower()
    is_genre_valid = (genre == 'drama') or (genre == 'comedy') or (genre == 'action') or (genre == 'romance') or (genre == 'science fiction') or (genre == 'horror') or (genre == 'fantasy') or (genre == 'thriller') or (genre == 'animation') or (genre == 'adventure')
    
    return is_genre_valid

def valid_rating(new_movie):
    is_rating_valid = ((new_movie.rating >= 0) and (new_movie.rating <= 10))
    
    return is_rating_valid

def valid_year(new_movie):
    is_year_valid = (new_movie.year >= 1888) and (new_movie.year <= 2023)
    
    return is_year_valid

def add_movie(movies_dict):
    new_movie = Movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
    new_movie.genre = new_movie.genre.lower()

    if (new_movie.genre == 'sci-fy'):
        new_movie.genre = 'science fiction'

    while ((valid_genre(new_movie) == False) or (valid_rating(new_movie) == False) or (valid_year(new_movie) == False)):
        
        if (valid_genre(new_movie) == False):
            print('')
            print('Invalid genre entered, try again...')

        elif (valid_rating(new_movie) == False):
            print('')
            print('Invalid rating entered, try again...')

        elif (valid_year(new_movie) == False):
            print('')
            print('Invalid year entered, try again...')
        
        new_movie = Movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
        new_movie.genre = new_movie.genre.lower()

    movies_dict[new_movie.title] = new_movie
    print('')


def movie_recommend(genre_input, movies_dict):
    genre_input = genre_input.lower()
    print('')
    print('RECOMMENDED MOVIE(S):')

    for title, movie in movies_dict.items():
        if (genre_input == movie.genre):
            print('____________________________')
            print('Title: ' + title)
            print('Rating:', movie.rating)
            print('____________________________')

# 10. Use the math package to round the average ratings to two decimal places.
def avg_genre_rating(genre_input, movies_dict):
    genre_array = []
    genre_input = genre_input.lower()

    for title in movies_dict:
        movie = movies_dict[title]

        if (genre_input == (movie.genre)):
            genre_array.append(movie.rating)

    print('Average rating for', genre_input, ':', np.mean(genre_array))

def export_dict(dict):
    json_dict = dict
    with open('movies.json', 'w') as file:
      json.dump(json_dict, file, cls=MovieEncoder)

def menu():
    print("___________________________________")
    print("_______________MENU:_______________")
    print()
    print("1. Movie recommendation.")
    print("2. Add a movie to the database.")
    print("3. Movie genre average rating.")
    print("___________________________________")
    print()
    menu_opt = int(input("Choose an option from the menu above: "))

    return menu_opt

def main():
    movies_dict = {}
    movies_dict = import_dict()

    menu_opt = menu()

    match(menu_opt):
        case 1:
            print()
            print("___________________________________")
            print("OPTION 1. MOVIE RECOMMENDATION")
            print()
            genre_input = input('Desired movie genre: ')
            movie_recommend(genre_input, movies_dict)

        case 2:
            print()
            print("___________________________________")
            print("OPTION 2. ADD A MOVIE TO THE DATABASE")
            print()

            confirm = str(input("Do you wish to add a movie (y/n)?"))
            confirm = confirm()
            confirm_add_movie = confirm == 'y'
            while confirm_add_movie:
                add_movie(movies_dict)
                count += 1    

                export_dict(movies_dict) 

                print("Movie database updated.") 
                confirm = str(input("Do you wish to add a movie (y/n)?"))
                confirm_add_movie = confirm == 'y'

        case 3:
            print()
            print("___________________________________")    
            print("OPTION 3. MOVIE GENRE AVERAGE RATING")
            print()
            genre_input = input('Desired movie genre: ')
            avg_genre_rating(genre_input, movies_dict)

main()
# 9. Write tests for all the implemented functions to ensure their correctness.