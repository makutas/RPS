from random import randint


def rps():
    print('Welcome to "Rock", "Paper", "Scissors" game!')
    player_points = 0
    computer_points = 0
    computer_variables = ['Rock', 'Paper', 'Scissors']
    player = input('Enter your name: ')

    while player_points != 3 and computer_points != 3:
        computer_choice = computer_variables[randint(0, 2)]
        player_choice = input(f'{player}: enter "Rock", "Paper", "Scissors" or type "quit": ')
        if player_choice == computer_choice:
            print(f"It's a tie!")
        elif player_choice == "Rock" and computer_choice == "Paper":
            computer_points += 1
            print(f'Paper covers rock! Computer wins! Computer has "{computer_points}" point(-s).')
        elif player_choice == "Rock" and computer_choice == "Scissors":
            player_points += 1
            print(f'Rock smashes scissors! {player} wins! {player} has "{player_points}" point(-s)')
        elif player_choice == "Paper" and computer_choice == "Scissors":
            computer_points += 1
            print(f'Scissors cuts paper! Computer wins! Computer has "{computer_points}" point(-s)')
        elif player_choice == "Paper" and computer_choice == "Rock":
            player_points += 1
            print(f'Paper covers rock! {player} wins! {player} has "{player_points}" point(-s)')
        elif player_choice == "Scissors" and computer_choice == "Rock":
            computer_points += 1
            print(f'Rock smashes scissors! Computer wins! Computer has "{computer_points} point(-s)!')
        elif player_choice == "Scissors" and computer_choice == "Paper":
            player_points += 1
            print(f'Scissors cut paper! {player} wins! Player has "{player_points}" point(-s)!')
        elif player_choice == "quit":
            print('Exiting game...')
            return
        else:
            print(f'You have entered "{player_choice}" - unknown command! Try again...')
    if player_points == 3:
        print('-'*100)
        print(f'You have accumulated {player_points} points!')
        print(f'Congratulations {player}!!! You won the match!')
    else:
        print('-'*100)
        print(f'Computer has accumulated {computer_points} point!')
        print(f'Sorry {player} - you were owned by computer...')


rps()
