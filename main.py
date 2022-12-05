"""                               STAR CINEMA HALL                                   """
""" -------------------------------------------------------------------------------- """
"""                        Created by : Md. Ashik Mahmud                             """
"""                        Contact : ashikmahmud1104@gmail.com                       """


class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, iD, movie_name, time):
        make_tuple = tuple((iD, movie_name, time))
        self.__show_list.append(make_tuple)
        l2d = []
        for i in range(self.__rows):
            temp = []
            for j in range(self.__cols):
                temp.append(chr(65 + i) + str(j))
            l2d.append(temp)

        self.__seats[iD] = l2d

    def view_show_list(self):
        print('--------------------------------------------------------------------------------------------------')
        for show in self.__show_list:
            print(f'MOVIE NAME: {show[1]}', end="")
            for m in range((30 - len(show[1]))):
                print(" ", end="")
            print(f'SHOW ID: {show[0]}', end="")
            for n in range((18 - len(show[0]))):
                print(" ", end="")
            print(f'TIME: {show[2]}')
        print('--------------------------------------------------------------------------------------------------')

    def view_available_seats(self, sid):
        found = False
        for show in self.__show_list:
            if sid == show[0]:
                found = True
                print(f'MOVIE NAME : {show[1]} \t\t TIME : {show[2]}')
                print('X for already booked seats.')
                print()
                print('--------------------------------------------------------------------------------')
                break

        if not found:
            print('------------------------------------------')
            print(f"ID - '{sid}' didn't match with any show")
            print('------------------------------------------')
            return

        for ID, SEATS in self.__seats.items():
            if sid == ID:
                for row in SEATS:
                    for col in row:
                        print(col, end="\t\t\t\t")
                    print()
                break
        print('--------------------------------------------------------------------------------')

    def book_seats(self, customer_name, mobile, show_id, seat_no_list, org_TL):
        for sid, seats in self.__seats.items():
            if sid == show_id:
                for p in seat_no_list:
                    if p[0] < 0 or p[0] > (self.__rows - 1) or p[1] < 0 or p[1] > (self.__cols - 1):
                        print('--------------------------------------------------------------')
                        print(f"INVALID SEAT NO - '{chr(65 + p[0]) + str(p[1])}' TRY AGAIN!!")
                        print('--------------------------------------------------------------')
                        print()
                        return

                for p in seat_no_list:
                    if seats[p[0]][p[1]] == 'X':
                        print('-------------------------------------------------')
                        print(f"'{chr(65 + p[0]) + str(p[1])}' is already booked")
                        print('-------------------------------------------------')
                        print()
                        return

                for t in org_TL:
                    chk = False
                    for seat in seats:
                        if t in seat:
                            chk = True
                            break
                    if not chk:
                        print('-----------------------------------------')
                        print(f"INVALID SEAT NO - '{t}' TRY AGAIN!!")
                        print('-----------------------------------------')
                        return

                tickets = []
                for p in seat_no_list:
                    tickets.append(seats[p[0]][p[1]])
                    seats[p[0]][p[1]] = 'X'

                print('##### TICKET BOOKED SUCCESSFULLY #####')
                print('------------------------------------------------------------')
                print()
                print(f'NAME : {customer_name}')
                print(f'PHONE NUMBER : {mobile}')
                print()
                for show in self.__show_list:
                    if show_id == show[0]:
                        print(f'MOVIE NAME : {show[1]} \t\t MOVIE TIME : {show[2]}')
                        break
                print('TICKETS : ', end="")
                for i in tickets:
                    print(i, end=" ")
                print()
                print(f'HALL : {self.__hall_no}')
                print()
                print('-----------------------------------------------------------')
                print()
                break


Star_cinema_1 = Hall(5, 5, 'SC-1001')
Star_cinema_1.entry_hall(Star_cinema_1)
Star_cinema_1.entry_show('m-100', 'The Imitation Game', 'Nov 15 2022 12:00 PM')
Star_cinema_1.entry_show('m-101', 'End Game', 'Nov 15 2022 06:00 PM')
Star_cinema_1.entry_show('m-102', 'Wakanda Forever', 'Nov 15 2022 09:00 PM')
print()

while True:
    print('1. VIEW ALL SHOWS TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    option = int(input('Enter option : '))

    if option == 1:
        Star_cinema_1.view_show_list()
        print()
    elif option == 2:
        show_id = input('Enter show Id : ')
        print()
        Star_cinema_1.view_available_seats(show_id)
        print()
    elif option == 3:
        name = input('ENTER CUSTOMER NAME : ')
        mobile = input('ENTER CUSTOMER MOBILE NUMBER : ')
        sid = input('ENTER SHOW ID : ')
        ticket = int(input('ENTER NUMBER OF TICKETS : '))
        org_tl = []
        ticket_list = []
        chk_string = '0123456789'
        chk = False
        for i in range(ticket):
            sn = input('ENTER SEAT NO : ')
            org_tl.append(sn)

            for char in sn[1:]:
                if char not in chk_string:
                    chk = True
                    print()
                    print('-----------------------------------------')
                    print(f"INVALID SEAT NO - '{sn}' TRY AGAIN!!")
                    print('-----------------------------------------')
                    break
            if chk:
                break
            make_t = tuple(((ord(sn[0]) - 65), int(sn[1:])))
            ticket_list.append(make_t)

        print()
        if not chk:
            Star_cinema_1.book_seats(name, mobile, sid, ticket_list, org_tl)
    else:
        break
