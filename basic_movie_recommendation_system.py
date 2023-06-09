import numpy as np
import json
import math

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

def import_dict():
    with open('movies.json', 'r') as json_file:
        movies_dict = json.load(json_file)

    return movies_dict

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

def genre_menu():
    print("___________________________________")
    print("_________GENRES AVAILABLE:_________")
    print()
    print(" 1. Drama")
    print(" 2. Comedy")
    print(" 3. Action")
    print(" 4. Romance")
    print(" 5. Science Fiction")
    print(" 6. Horror")
    print(" 7. Fantasy")
    print(" 8. Thriller")
    print(" 9. Animation")
    print("10. Adventure")
    print("___________________________________")
    
    genre_opt_num = int(input("Choose an option from the menu above: "))

    return genre_opt_num

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

    for movie_dict2 in movies_dict.values():
        for movie in movie_dict2.values():
            movie_obj = Movie(*movie)

            if genre_input == movie_obj.genre:
                print('____________________________')
                print('Title: ', movie_obj.title)
                print('Rating:', movie_obj.rating)
                print('Year:', movie_obj.year)            
                print('____________________________')

def avg_genre_rating(genre_input, movies_dict):
    genre_array = []
    genre_input = genre_input.lower()

    for movies_dict2 in movies_dict.values():
        for movie in movies_dict2.values():
            movie_obj = Movie(*movie)

            if (genre_input == (movie_obj.genre)):
                genre_array.append(movie_obj.rating)

    avg_rating = np.mean(genre_array)
    avg_rating = round(avg_rating, 2)

    print('Average rating for', genre_input, ':', avg_rating)

def export_dict(dict):
    json_dict = dict
    with open('movies.json', 'w') as file:
      json.dump(json_dict, file, cls=MovieEncoder)

def genre_opt_convert(genre_opt_num):
    match (genre_opt_num):
        case 1:
            genre_opt = "drama"
        case 2:
            genre_opt = "comedy"            
        case 3:
            genre_opt = "action"
        case 4:
            genre_opt = "romance"
        case 5:
            genre_opt = "science fiction"
        case 6:
            genre_opt = "horror"
        case 7:
            genre_opt = "fantasy"
        case 8:
            genre_opt = "thriller"
        case 9:
            genre_opt = "animation"
        case 10:
            genre_opt = "adventure"

    return genre_opt

def main():
    movies_dict = {}
    movies_dict = import_dict()

    menu_opt = menu()
    while ((menu_opt < 1) or (menu_opt > 3)):
        print("")
        print("Invalid option entered.")
        print("Try again...")
        menu_opt = menu()

    match(menu_opt):
        case 1:
            print()
            print("___________________________________")
            print("OPTION 1. MOVIE RECOMMENDATION")
            print()
            
            genre_input_num = int(genre_menu())
            
            while (genre_input_num < 1) or (genre_input_num > 10):
                genre_input = int(genre_menu())

            genre_input = genre_opt_convert(genre_input_num)
            movie_recommend(genre_input, movies_dict)

        case 2:
            print()
            print("___________________________________")
            print("OPTION 2. ADD A MOVIE TO THE DATABASE")
            print()

            confirm = str(input("Do you wish to add a movie (y/n)?"))
            confirm = confirm[:1].lower()
            confirm_add_movie = confirm == 'y'

            while confirm_add_movie:
                add_movie(movies_dict)

                export_dict(movies_dict) 

                print("Movie database updated.") 
                confirm = str(input("Do you wish to add a movie (y/n)? "))
                confirm_add_movie = confirm == 'y'

            if confirm_add_movie == False:
                print("Exiting Movie System...")         

        case 3:
            print()
            print("___________________________________")    
            print("OPTION 3. MOVIE GENRE AVERAGE RATING")
            print()
          
            genre_input_num = int(genre_menu())
            
            while (genre_input_num < 1) or (genre_input_num > 10):
                genre_input = int(genre_menu())

            genre_input = genre_opt_convert(genre_input_num)

            avg_genre_rating(genre_input, movies_dict)

main()
# 9. Write tests for all the implemented functions to ensure their correctness.