def box_office(genre):
    match genre:
        case 1: # drama
            movie = ['Killers of the Flower Moon','Drama',2023,0]
        case 2: # comedy
            movie = ['Barbie','Comedy',2023,0]
        case 3: # action
            movie = ['Fast X','Action',2023,6.3]
        case 4: # romance
            movie = ['The Little Mermaid','Romance',2023,7.0]
        case 5: # sci-fy
            movie = ['Ant-Man and the Wasp: Quantumania','Sci-fy',2023,6.2]
        case 6: # horror
            movie = ['Evil Dead Rise','Horror',2023,6.7]
        case 7: # fantasy
            movie = ['The Super Mario Bros. Movie','Fantasy',2023,7.2]
        case 8: # thriller
            movie = ['John Wick: Chapter 4','Thriller',2023,8]
        case 9: # animation
            movie = ['Spider-Man: Across the Spider-Verse','Animation',2023,0]
        case 10: # adventure
            movie = ['Guardians of the Galaxy Vol. 3','Adventure',2023,8.2]

    return movie

def top_250(genre):
    match genre:
        case 1: # drama
            movie = ['The Shawshank Redemption','Drama',1994,9.3]
        case 2: # comedy
            movie = ['Modern Times','Comedy',1936,8.5]
        case 3: # action
            movie = ['The Dark Knight','Action',2008,9.0]
        case 4: # romance
            movie = ['Before Sunrise','Romance',1995,8.1]
        case 5: # sci-fy
            movie = ['Interstelar','Sci-fy',2014,8.7]
        case 6: # horror
            movie = ['The shining','Horror',1980,8.4]
        case 7: # fantasy
            movie = ['Spirited Away','Fantasy',2001,8.6]
        case 8: # thriller
            movie = ['Se7en','Thriller',1995,8.6]
        case 9: # animation
            movie = ['The Lion King','Animation',1994,8.5]
        case 10: # adventure
            movie = ['The Lord of the Rings: The Return of the King','Adventure',2003,9.0]

    return movie