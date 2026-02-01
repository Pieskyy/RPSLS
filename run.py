import random

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def checker(player_input):
    if player_input not in options:
        print('Not an option.')
        return False
    return True

def logic(player_input, bot_input):
    wins_against = {
        'rock':{'scissors', 'lizard'},
        'paper':{'rock', 'spock'},
        'scissors':{'paper', 'lizard'},
        'lizard':{'spock', 'paper'},
        'spock':{'scissors', 'rock'}
    }

    if player_input == bot_input:
        print('Tie!')
    elif bot_input in wins_against[player_input]:
        print('Win!')
    else:
        print('Lost :(')


while True:
    player_input = input("Type either 'Rock', 'Paper', 'Scissors', 'Lizard', or 'Spock' (or 'q' to quit): ").lower()

    if player_input == 'q':
        break

    if not checker(player_input):
        continue

    bot_input = random.choice(options)
    print("Bot chose:", bot_input)

    logic(player_input, bot_input)
