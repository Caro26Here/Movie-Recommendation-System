import numpy as np
import json

class MovieEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Movie):
            movieDict = {
                obj.title : [obj.title, obj.genre, obj.rating, obj.year]
            }
            return movieDict
        return super().default(obj)
    
class Movie:
    def __init__(self, title, genre, rating, year):
        self.title = str(title)
        self.genre = str(genre)
        self.rating = float(rating)
        self.year = int(year)

def importDictionary():
    with open('movies.json', 'r') as jsonFile:
        moviesDict = json.load(jsonFile)

    return moviesDict

def menu():
    print("_____________________________________")
    print("________________MENU:________________")
    print()
    print("1. Movie recommendation.")
    print("2. Add a movie to the database.")
    print("_____________________________________")
    print()
    menuOption = int(input("Choose an option from the menu above: "))

    return menuOption

def genreMenu():
    print("_____________________________________")
    print("__________GENRES AVAILABLE:__________")
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
    print("_____________________________________")
    print()

    genreOption = int(input("Choose an option from the menu above: "))

    return genreOption

def validGenre(newMovie):
    genre = newMovie.genre.lower()
    isGenreValid = (genre == 'drama') or (genre == 'comedy') or (genre == 'action') or (genre == 'romance') or (genre == 'science fiction') or (genre == 'horror') or (genre == 'fantasy') or (genre == 'thriller') or (genre == 'animation') or (genre == 'adventure')
    
    return isGenreValid

def validRating(newMovie):
    isRatingValid = ((newMovie.rating >= 0) and (newMovie.rating <= 10))
    
    return isRatingValid

def validYear(newMovie):
    isYearValid = (newMovie.year >= 1888) and (newMovie.year <= 2023)
    
    return isYearValid

def addMovie(moviesDict):
    newMovie = Movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
    newMovie.genre = newMovie.genre.lower()

    if (newMovie.genre == 'sci-fy'):
        newMovie.genre = 'science fiction'

    while ((validGenre(newMovie) == False) or (validRating(newMovie) == False) or (validYear(newMovie) == False)):
        
        if (validGenre(newMovie) == False):
            print('')
            print('Invalid genre entered, try again...')

        elif (validRating(newMovie) == False):
            print('')
            print('Invalid rating entered, try again...')

        elif (validYear(newMovie) == False):
            print('')
            print('Invalid year entered, try again...')
        
        newMovie = Movie(input('Title: '), input('Genre: '), input('Rating: '), input('Year: '))
        newMovie.genre = newMovie.genre.lower()

    moviesDict[newMovie.title] = newMovie
    print('')

def validOption(opt):
    while True:
        try:
            if type(opt) == int:
                return opt
        except ValueError:
            print("Invalid Option Entered. Please try again.")

def movieRecommend(genreInput, moviesDict):
    genreInput = genreInput.lower()
    print('')
    print("_____________________________________")
    print('RECOMMENDED MOVIE(S):')

    genreDictionary ={}
    for movieDict2 in moviesDict.values():
        for movie in movieDict2.values():
            movieObject = Movie(*movie)

            if genreInput == movieObject.genre:
                genreDictionary[movieObject.title] = movieObject

    sortedGenreList = sorted(genreDictionary.items(), key=lambda item: item[1].rating, reverse=True)
    sortedDictionary = {k: v for k, v in sortedGenreList}
    
    cont = 0
    for movieObject in sortedDictionary.values():
        
        if cont < 3:
            print("_____________________________________")
            print('Title: ', movieObject.title)
            print('Rating:', movieObject.rating)
            print('Year:', movieObject.year)            
            print("_____________________________________")
            cont += 1

def exportDictionary(dict):
    jsonDictionary = dict
    with open('movies.json', 'w') as file:
      json.dump(jsonDictionary, file, cls=MovieEncoder)

def genreOptionConverter(genreOption):
    match (genreOption):
        case 1:
            genreOption = "drama"
        case 2:
            genreOption = "comedy"            
        case 3:
            genreOption = "action"
        case 4:
            genreOption = "romance"
        case 5:
            genreOption = "science fiction"
        case 6:
            genreOption = "horror"
        case 7:
            genreOption = "fantasy"
        case 8:
            genreOption = "thriller"
        case 9:
            genreOption = "animation"
        case 10:
            genreOption = "adventure"

    return genreOption

def main():
    moviesDict = {}
    moviesDict = importDictionary()

    menuOption = menu()
    while ((menuOption < 1) or (menuOption > 3)):
        print("")
        print("Invalid option entered.")
        print("Try again...")
        menuOption = menu()

    match(menuOption):
        case 1:
            print()
            print("_____________________________________")
            print("OPTION 1. MOVIE RECOMMENDATION")
            
            genreInputNum = int(genreMenu())
            
            while (genreInputNum < 1) or (genreInputNum > 10):
                genreInput = int(genreMenu())

            validOption(genreInputNum)
            
            genreInput = genreOptionConverter(genreInputNum)
            movieRecommend(genreInput, moviesDict)

        case 2:
            print()
            print("_____________________________________")
            print("OPTION 2. ADD A MOVIE TO THE DATABASE")
            print()

            confirm = str(input("Do you wish to add a movie (y/n)?"))
            confirm = confirm[:1].lower()
            confirmAddMovie = confirm == 'y'

            while confirmAddMovie:
                addMovie(moviesDict)

                exportDictionary(moviesDict) 

                print("Movie database updated.") 
                confirm = str(input("Do you wish to add a movie (y/n)? "))
                confirmAddMovie = confirm == 'y'

            if confirmAddMovie == False:
                print("Exiting Movie System...")         


main()
# 9. Write tests for all the implemented functions to ensure their correctness.