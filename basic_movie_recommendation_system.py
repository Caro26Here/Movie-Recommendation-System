import numpy as np

# 1. Create a class called Movie with the following attributes: title, genre, rating, and year.
class movie:
    def __init__(self, title, genre, rating, year): # read about class constructor (python).
        self.title = str(title)
        self.genre = str(genre)
        self.rating = float(rating)
        self.year = int(year)

    # 2. Implement methods in the Movie class to set and get the attributes.
    # This initially becomes redundant when declaring them in the constructor method of the class.
    # It is recommended when further logic and complex programming takes place.
    # def set_movie(self):
    #     pass
    
    # This initially becomes redundant when declaring them in the constructor method of the class.
    # It is recommended when further logic and complex programming takes place.
    # def get_movie(self):
    #     pass

# To check dictionary structure:        
# movie1 = movie('Inception', 'Science Fiction', 8.8, 2010)
# print('Movie:', movie1.title)
# print('Genre:', movie1.genre)
# print('')

# 4. Implement a function to add movies to the system. The function should take movie 
# information as input and create a Movie object, storing it in the movie dictionary.
def valid_genre(new_movie):
    is_genre_valid = (new_movie.genre == 'Drama') or (new_movie.genre == 'Comedy') or (new_movie.genre == 'Action') or (new_movie.genre == 'Romance') or (new_movie.genre == 'Sci-fy') or (new_movie.genre == 'Horror') or (new_movie.genre == 'Fantasy') or (new_movie.genre == 'Thriller') or (new_movie.genre == 'Animation') or (new_movie.genre == 'Adventure')
    
    return is_genre_valid

def valid_rating(new_movie):
    is_rating_valid = ((new_movie.rating >= 0) and (new_movie.rating <= 10))
    
    return is_rating_valid

def valid_year(new_movie):
    is_year_valid = (new_movie.year >= 0) and (new_movie.year <= 2023)
    
    return is_year_valid

def add_movie(movies_dict):
    new_movie = movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
    new_movie.genre = new_movie.genre.capitalize()

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
        
        new_movie = movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
        new_movie.genre = new_movie.genre.capitalize()

    movies_dict[new_movie.title] = new_movie
    print('')
    #movies_dict.append(new_movie)

# 3. Use a dictionary to store movie information, where the movie title is the key, 
# and the Movie object is the value.
count = 0
movies_dict = {}
while count < 3:
    #new_movie = movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
    #movies_dict = {(new_movie.title): new_movie}
    add_movie(movies_dict)
    count += 1

# Check the current working directory by printing it:
# for title, new_movie in movies_dict.items():
#     print('Title:' + new_movie.title)
#     print('Genre:' + new_movie.genre)
#     print('')

# 5. Implement a function to recommend movies to a user based on their preferred genre. The
# function should take a genre as input and return a list of movies with the highest ratings 
# in that genre.
def movie_recommend(genre_input, movies_dict):
    genre_input = genre_input.capitalize()
    print('')
    print('RECOMMENDED MOVIE(S):')

    for title, movie in movies_dict.items():
        if (genre_input == movie.genre):
            print('____________________________')
            print('Title: ' + title)
            print('Rating:', movie.rating)
            print('____________________________')

genre_input = input('Desired movie genre: ')
genre_input = genre_input.capitalize()
movie_recommend(genre_input, movies_dict)

# 6. Use the NumPy package to calculate the average rating for movies in a given genre.
# 10. Use the math package to round the average ratings to two decimal places.
def avg_genre_rating(genre_input, movies_dict):
    genre_array = []

    for title in movies_dict:
        movie = movies_dict[title]

        if (genre_input == (movie.genre)):
            genre_array.append(movie.rating)

    print('Average rating for', genre_input, ':', np.mean(genre_array))

avg_genre_rating(genre_input, movies_dict)

# 7. Implement a function to export the movie dictionary to a JSON file.
def export_updated_dict():
    pass

# 8. Implement a function to import movie information from a JSON file and update the movie 
# dictionary accordingly.
def import_dict():
    pass

# 9. Write tests for all the implemented functions to ensure their correctness.

