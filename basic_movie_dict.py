def box_office(genre):
    match genre:
        case 1: # drama
            movie = ['Killers of the Flower Moon', 'Drama', 0, 2023]
        case 2: # comedy
            movie = ['Barbie', 'Comedy', 0, 2023]
        case 3: # action
            movie = ['Fast X', 'Action', 6.3, 2023]
        case 4: # romance
            movie = ['The Little Mermaid', 'Romance', 7.0, 2023]
        case 5: # sci-fy
            movie = ['Ant-Man and the Wasp: Quantumania', 'Sci-fy', 6.2, 2023]
        case 6: # horror
            movie = ['Evil Dead Rise', 'Horror', 6.7, 2023]
        case 7: # fantasy
            movie = ['The Super Mario Bros. Movie', 'Fantasy', 7.2, 2023]
        case 8: # thriller
            movie = ['John Wick: Chapter 4', 'Thriller', 8, 2023]
        case 9: # animation
            movie = ['Spider-Man: Across the Spider-Verse', 'Animation', 0, 2023]
        case 10: # adventure
            movie = ['Guardians of the Galaxy Vol. 3', 'Adventure', 8.2, 2023]

    return movie

def top_250(genre):
    match genre:
        case 1: # drama
            movie = ['The Shawshank Redemption', 'Drama', 9.3, 1994]
        case 2: # comedy
            movie = ['Modern Times', 'Comedy', 8.5, 1936]
        case 3: # action
            movie = ['The Dark Knight', 'Action', 9.0, 2008]
        case 4: # romance
            movie = ['Before Sunrise', 'Romance', 8.1, 1995]
        case 5: # sci-fy
            movie = ['Interstelar', 'Sci-fy', 8.7, 2014]
        case 6: # horror
            movie = ['The shining', 'Horror', 8.4, 1980]
        case 7: # fantasy
            movie = ['Spirited Away', 'Fantasy', 8.6, 2001]
        case 8: # thriller
            movie = ['Se7en', 'Thriller', 8.6, 1995]
        case 9: # animation
            movie = ['The Lion King', 'Animation', 8.5, 1994]
        case 10: # adventure
            movie = ['The Lord of the Rings: The Return of the King', 'Adventure', 9.0, 2003]

    return movie