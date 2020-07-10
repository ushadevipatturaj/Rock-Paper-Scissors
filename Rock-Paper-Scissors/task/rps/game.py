import random


def find_probability(userchoice, listchoice, computerchoice):
    global score
    if userchoice == 'scissors':
        if computerchoice in ['fire', 'rock', 'water', 'dragon', 'devil', 'lightning', 'gun']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'rock':
        if computerchoice in ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'paper':
        if computerchoice in ['fire', 'tree', 'snake', 'scissors', 'human', 'wolf', 'sponge']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'fire':
        if computerchoice in ['air', 'rock', 'water', 'devil', 'dragon', 'gun', 'lightning']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'snake':
        if computerchoice in ['fire', 'rock', 'scissors', 'devil', 'dragon', 'gun', 'lightning']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'human':
        if computerchoice in ['fire', 'rock', 'scissors', 'devil', 'snake', 'gun', 'lightning']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'tree':
        if computerchoice in ['fire', 'rock', 'scissors', 'human', 'snake', 'gun', 'lightning']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'wolf':
        if computerchoice in ['fire', 'rock', 'scissors', 'human', 'snake', 'gun', 'tree']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'sponge':
        if computerchoice in ['wolf', 'rock', 'scissors', 'human', 'snake', 'fire', 'tree']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'air':
        if computerchoice in ['wolf', 'paper', 'sponge', 'human', 'snake', 'fire', 'scissors']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'water':
        if computerchoice in ['wolf', 'sponge', 'human', 'air', 'paper', 'snake', 'tree']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'dragon':
        if computerchoice in ['wolf', 'water', 'air', 'sponge', 'paper', 'human', 'tree']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'devil':
        if computerchoice in ['wolf', 'sponge', 'paper', 'tree', 'air', 'water', 'dragon']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'lightning':
        if computerchoice in ['wolf', 'sponge', 'paper', 'devil', 'air', 'water', 'dragon']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))
    elif userchoice == 'gun':
        if computerchoice in ['lightning', 'sponge', 'paper', 'tree', 'air', 'water', 'dragon']:
            print('Sorry, but computer chose', computerchoice)
        else:
            score += 100
            print('Well done. Computer chose {} and failed'.format(computerchoice))


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
list_choice_input = input()
if list_choice_input == '':
    list_choice = ['rock', 'paper', 'scissors']
else:
    list_choice = list_choice_input.split(",")
print("Okay, let's start")
while run:

    user_choice = input()
    computer_choice = random.choice(list_choice)
    if user_choice == '!rating':
        print('Your rating:', score)
    elif user_choice == '!exit':
        run = False
        print('!Bye')
        exit(0)
    elif user_choice == computer_choice:
        print('There is a draw ({})'.format(user_choice))
        score += 50
    elif user_choice in list_choice:
        find_probability(user_choice, list_choice, computer_choice)
    else:
        print('Invalid input')


