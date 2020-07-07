import random

run = True
# Write your code here
while run:

    user_choice = input()
    list_choice = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(list_choice)
    if user_choice == computer_choice:
        print('There is a draw ({})'.format(user_choice))
    elif user_choice in list_choice or user_choice == '!exit':
        if user_choice == 'scissors':
            if computer_choice == 'rock':
                print('Sorry, but computer chose rock')
            elif computer_choice == 'paper':
                print('Well done. Computer chose paper and failed')
        elif user_choice == 'rock':
            if computer_choice == 'paper':
                print('Sorry, but computer chose paper')
            elif computer_choice == 'scissors':
                print('Well done. Computer chose scissors and failed')
        elif user_choice == 'paper':
            if computer_choice == 'scissors':
                print('Sorry, but computer chose scissors')
            elif computer_choice == 'rock':
                print('Well done. Computer chose rock and failed')
        elif user_choice == '!exit':
            run = False
            print('!Bye')
            exit(0)

    else:
        print('Invalid input')
