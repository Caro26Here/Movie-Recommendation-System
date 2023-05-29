from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
""" movie = ia.get_movie('0133093')

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

# search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name']) """

top = ia.get_top50_movies_by_genres('drama')
print('______________')
print('DRAMA:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('comedy')
print('______________')
print('COMEDY:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('action')
print('______________')
print('ACCTION:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('romance')
print('______________')
print('ROMANCE:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('scify')
print('______________')
print('SCIENCE FICTION:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('horror')
print('______________')
print('HORROR:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('fantasy')
print('______________')
print('FANTASY:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('thriller')
print('______________')
print('THRILLER:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('animation')
print('______________')
print('ANIMATION:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

top = ia.get_top50_movies_by_genres('adventure')
print('______________')
print('ADVENTURE:')
print(top[0])
print(top[1])
print(top[2])
print('______________')

movie = ia.search_movie_advanced('matrix')
movie = movie[0]
movie.current_info

# <Movie id:0133093[http] title:_The Matrix (1999)_>