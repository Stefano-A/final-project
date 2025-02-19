def display_film_info(dict_screening):
    for info_key, info_value in dict_screening.items():
        print(f'{info_key}: {info_value}')
    print()
def book_seats(dict_screen_selected):
        movie_number_selected = dict_screen_selected.get('movie number')
        print('\nSELECTED MOVIE IS:')
        display_film_info(dict_screen_selected)

        n_seats = dict_screen_selected.get('availabe seats')
        print(f'The number of available seats for this movie is: {n_seats}')
        seat_reservation = int(input('Enter the number of seats you want to book: '))
    
        if n_seats - seat_reservation >= 0:
            dict_screen_selected['availabe seats'] -= seat_reservation
            reservations.update({movie_number_selected:seat_reservation})
            print('Seats reservation completed\n')
        else:
            print('There are not enough seats available\n')
def change_seats(reservations, screening_list, selection):
    change = int(input('Enter the new number of seats you want to reserve: '))
    screening_list[selection-1]['availabe seats'] += reservations.get(selection)
    seats_reset = screening_list[selection-1]['availabe seats']
    if seats_reset - change >= 0:
        screening_list[selection-1]['availabe seats'] -= change
        reservations[selection] = change
        print(f'Reservation for movie number {selection} has changed. New seats reserved: {change}\n')
    else:
        print('There are not enough seats available\n')
def check_reservation(reservations,screening_list):
                print('You have a reservation for:')
                for res in reservations:
                    mov_num = screening_list[res-1]['movie number']
                    title = screening_list[res-1]['title']
                    av_seats = screening_list[res-1]['availabe seats']
                    res_seats = reservations.get(res)
                    print(f'Movie number: {mov_num}')
                    print(f'Title: {title}')
                    print(f'Available seats: {av_seats}')
                    print(f'Seats reserved: {res_seats}\n')
                return res    
screening_1 = {
    'movie number' : 1,
    'title' : 'Rambo',
    'time' : 120,
    'theater' : 'Red cinema',
    'availabe seats' : 1500
}
screening_2 = {
    'movie number' : 2,
    'title' : 'Spiderman',
    'time' : 140,
    'theater' : 'Blue cinema',
    'availabe seats' : 1800
}
screening_3 = {
    'movie number' : 3,
    'title' : 'Star Wars',
    'time' : 105,
    'theater' : 'Green cinema',
    'availabe seats' : 1100
}

screening_list = [screening_1, screening_2, screening_3]
reservations = {}
n_films = len(screening_list)
is_continue = True

while is_continue:
    main_menu = input('Select one of these options by entering the corresponding number:\n 1) New reservation\n 2) Change reservation\n 3) Delete reservation\n 4) Display movies information\n 5) Exit(default).\n: ' )
    # new reservation
    if main_menu == '1':
        print(f'There are {n_films} movies in the list.')
        selected_film = int(input(f'Select the number corresponding to the film you want to reserve: ')) -1
        if 0 <= selected_film < n_films:
            if selected_film + 1 in reservations:
                print('You already have a reservation for this movie.')
            else:
                book_seats(screening_list[selected_film])
        else:
            print('no match with movie number')
    # change reservation
    elif main_menu == '2':
        number_of_res = len(reservations)
        if number_of_res == 0:
            print('There are no reservations. Please, make a new reservation first.\n')
        else:
            res = check_reservation(reservations,screening_list)            
            if number_of_res == 1:
                change_seats(reservations,screening_list,res)
            else:
                choose = int(input('Select the number of the movie you want to change the reservation for: '))
                if choose in reservations:
                    change_seats(reservations,screening_list,choose)
                else:
                    print('There are no reservations for this movie')
    # delete reservation
    elif main_menu == '3':
        number_of_res = len(reservations)
        if number_of_res == 0:
            print('There are no reservations to delete.\n')
        else:
            check_reservation(reservations,screening_list)            
            if number_of_res == 1:
                for res in reservations:
                    screening_list[res-1]['availabe seats'] += reservations.get(res)
                reservations.clear()
                print('The reservation has been deleted\n')
            else:
                choose = int(input('Select the number of the movie you want to delete the reservation for: '))
                if choose in reservations:
                        screening_list[choose-1]['availabe seats'] += reservations.get(choose)
                        reservations.pop(choose)
                        print('The reservation has been deleted')
                else:
                    print('There are no reservations for this movie')
    elif main_menu == '4':
        for film in screening_list:
            display_film_info(film)
    else:
        print('The program will exit')
        is_continue = False
        