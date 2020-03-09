def rps():
    points_p1 = 0
    points_p2 = 0
    print('Welcome to "Rock", "Paper", "Scissors" game!')
    p1 = input('Enter your name player 1 : ')
    p2 = input('Enter your name player 2 : ')
    while points_p1 != 3 and points_p2 != 3:
        p1_choice = input(f'{p1}: enter "r", "p", "s" or type "quit" to quit: ')
        while True:
            if p1_choice == "quit":
                print(f'{p1} entered "quit".\nExiting...')
                return
            elif p1_choice != "r" and p1_choice != "p" and p1_choice != "s":
                print('Unknown command! Try again...')
                p1_choice = input(f'{p1}: enter "r", "p", "s" or type "quit" to quit: ')
                continue
            else:
                break
        p2_choice = input(f'{p2}: enter "r", "p", "s" or type "quit" to quit: ')
        while True:
            if p2_choice == "quit":
                print(f'{p2} entered "quit".\nExiting....')
                return
            elif p2_choice != "r" and p2_choice != "p" and p2_choice != "s":
                print('Unknown command! Try again...')
                p2_choice = input(f'{p2}: enter "r", "p", "s" or type "quit" to quit: ')
            else:
                break
        if p1_choice == p2_choice:
            print(f"It's a tie!")
        elif p1_choice == "r" and p2_choice == "p":
            points_p2 += 1
            print(f'{p2} wins and has "{points_p2}" point(-s)!')
        elif p1_choice == "r" and p2_choice == "s":
            points_p1 += 1
            print(f'{p1} wins and has "{points_p1}" point(-s)!')
        elif p1_choice == "p" and p2_choice == "s":
            points_p2 += 1
            print(f'{p2} wins and has "{points_p2}" point(-s)!')
        elif p1_choice == "p" and p2_choice == "r":
            points_p1 += 1
            print(f'{p1} wins and has "{points_p1}" point(-s)!')
        elif p1_choice == "s" and p2_choice == "r":
            points_p2 += 1
            print(f'{p2} wins and has "{points_p2}" point(-s)!')
        elif p1_choice == "s" and p2_choice == "p":
            points_p1 += 1
            print(f'{p1} wins and has "{points_p1}" point(-s)!')
    if points_p1 == 3:
        print(f'Congratulations {p1}!!! You won the match!')
    else:
        print(f'Congratulations {p2}!!! You own the match!')


rps()
