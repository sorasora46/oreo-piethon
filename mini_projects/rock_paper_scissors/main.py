# rock paper scissors game
import random

ROCK = 1
PAPER = 2
SCISSORS = 3

def show_menu(round):
    print('-'*20)
    print('Round: ' + str(round))
    print('Choose your weapon! (no. 1 - 3)')
    print('[1] Rock')
    print('[2] Paper')
    print('[3] Scissors')
    print('-'*20)

def find_winner(u_weapon, b_weapon):
    if u_weapon == ROCK and b_weapon == PAPER:
        return 'BOT'
    if u_weapon == ROCK and b_weapon == SCISSORS:
        return 'USER'
    if u_weapon == ROCK and b_weapon == ROCK:
        return 'DRAW'

    if u_weapon == PAPER and b_weapon == PAPER:
        return 'DRAW'
    if u_weapon == PAPER and b_weapon == SCISSORS:
        return 'BOT'
    if u_weapon == PAPER and b_weapon == ROCK:
        return 'USER'

    if u_weapon == SCISSORS and b_weapon == PAPER:
        return 'USER'
    if u_weapon == SCISSORS and b_weapon == SCISSORS:
        return 'DRAW'
    if u_weapon == SCISSORS and b_weapon == ROCK:
        return 'BOT'

def get_bot_weapon(b_weapon):
    if b_weapon == ROCK:
        return 'Rock'
    if b_weapon == PAPER:
        return 'Paper'
    return 'Scissors'

def play():
    user_score = 0
    bot_score = 0
    round = int(input('Enter how many round you want to compete: '))

    for i in range(round):
        show_menu(i + 1)

        bot_weapon = random.randint(1,3)
        user_weapon = 0
        while user_weapon < 1 or user_weapon > 3:
            user_weapon = int(input('Your choice: '))

        result = find_winner(user_weapon, bot_weapon)

        if result == 'USER':
            user_score += 1
        if result == 'BOT':
            user_score += 1

        if result == 'DRAW':
            print('Bot weapon: ' + get_bot_weapon(bot_weapon))
            print(result)
        else:
            print('Bot weapon: ' + get_bot_weapon(bot_weapon))
            print(result + ' win!')
    
    winner = ''
    winner_score = 0
    if user_score == bot_score:
        winner = 'DRAW'
        winner_score = user_score
    if user_score > bot_score:
        winner = 'USER'
        winner_score = user_score
    if user_score < bot_score:
        winner = 'BOT'
        winner_score = bot_score
    
    print('-'*20)
    print('The winner is ' + winner)
    print('With a score of ' + str(winner_score))

play()