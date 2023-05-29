def menu_opt():
    print('___________________________')
    print('GENRE MENU:')
    print('1. Drama')
    print('2. Comedy')
    print('3. Action')
    print('4. Romance')
    print('5. Science Fiction')
    print('6. Horror')
    print('7. Fantasy')
    print('8. Thriller')
    print('9. Animation')
    print('10. Adventure')
    print('___________________________')
    print()
    genre = int(input('Enter the desired genre option: '))
    cont = 1

    while (cont < 3) and ((genre < 1) or (genre > 10)):
        print('Option entered is not in the menu above. Try again')
        genre = int(input('Enter the desired genre option: '))
        cont += 1

    return genre

def moviefunc(genre):
    match genre:
        case 1: # drama
            movie = ['Killers of the Flower Moon','Drama',2023,'tba']
        case 2: # comedy
            movie = ['Barbie','Comedy',2023,'tba']
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
            movie = ['Spider-Man: Across the Spider-Verse','Animation',2023,'tba']
        case 10: # adventure
            movie = ['Guardians of the Galaxy Vol. 3','Comedy',2023,8.2]

    return movie

def main():
    genre = menu_opt()
    movie = moviefunc(genre)

    print()
    print('___________________________')
    print('BOX OFFICE RECOMMENDATION:')
    for i in range(len(movie)):
        print(movie[i])
    print('___________________________')

main()