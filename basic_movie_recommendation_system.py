import numpy as np

# 1. Create a class called Movie with the following attributes: title, genre, rating, and year.
class movie:
    def __init__(self, title, genre, rating, year): # read about class constructor (python).
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

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
def add_movie(movies_dict):
    new_movie = movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
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
    genre_input
    
    for title, movie in movies_dict.items():
        if (genre_input == movie.genre):
            print('____________________________')
            print('RECOMMENDED MOVIE:')
            print('Title:' + title)
            print('Rating:' + movie.rating)
            print('____________________________')

genre_input = input('Desired movie genre: ')
movie_recommend(genre_input, movies_dict)

# 6. Use the NumPy package to calculate the average rating for movies in a given genre.

# 7. Implement a function to export the movie dictionary to a JSON file.

# 8. Implement a function to import movie information from a JSON file and update the movie 
# dictionary accordingly.

# 9. Write tests for all the implemented functions to ensure their correctness.

# 10. Use the math package to round the average ratings to two decimal places.