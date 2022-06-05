from random import random

while True:

    options = ['R', 'P', 'S']
    user = input('pick your option from the list: ').upper()


    while user not in options:
        print('invalid option')
        user = input('pick your option from the list: ').upper()


    if user == 'R':
        user_choice = 'rock'
        
    elif user == 'P':
        user_choice = 'paper'

    elif user == 'S':
        user_choice = 'scissors'

    computer = random.choice(options)

    if computer == 'R':
        computer_choice = 'rock'

    elif computer == 'P':
        computer_choice = 'paper'

    elif computer == 'S':
        computer_choice = 'scissors'

        print(f"user's choice is ({user_choice}) : computer's choice is ({computer_choice}) ")


        if (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'P' and computer_choice == 'R'):
            print("paper wins")

        elif (user_choice == 'S' and computer_choice == 'P') or (user_choice== 'R' and computer_choice == 'S'):
            print('computer wins')




