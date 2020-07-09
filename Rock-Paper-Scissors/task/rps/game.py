import random


def read_file(user):
    score_file = open('rating.txt', 'r')
    for line in score_file:
        name, value = line.split(' ')
        if name == user:
            return int(value)
        else:
            return 0


run = True
# Write your code here
print('Enter your name:')
username = input()
print('Hello, {}'.format(username))
score = read_file(username)
while run:

    user_choice = input()
    list_choice = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(list_choice)
    if user_choice == '!rating':
        print('Your rating:', score)
    elif user_choice == '!exit':
        run = False
        print('!Bye')
        exit(0)
    elif user_choice in list_choice:
        if user_choice == computer_choice:
            print('There is a draw ({})'.format(user_choice))
            score += 50
        else:
            if user_choice == 'scissors':
                if computer_choice == 'rock':
                    print('Sorry, but computer chose rock')
                elif computer_choice == 'paper':
                    score += 100
                    print('Well done. Computer chose paper and failed')
            elif user_choice == 'rock':
                if computer_choice == 'paper':
                    print('Sorry, but computer chose paper')
                elif computer_choice == 'scissors':
                    score += 100
                    print('Well done. Computer chose scissors and failed')
            elif user_choice == 'paper':
                if computer_choice == 'scissors':
                    print('Sorry, but computer chose scissors')
                elif computer_choice == 'rock':
                    score += 100
                    print('Well done. Computer chose rock and failed')
    else:
        print('Invalid input')
