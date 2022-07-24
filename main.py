# This is a sample Python script.

import random


def play():
    user = input(" 'r' for rock, 'p' paper 's' scissor: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'its a tie'

    if winner(user, computer):
        return 'You won'

    else:
        return 'you lost'


# s > p , p > r , r > s
def winner(player, opponent):
    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (
            player == 'r' and opponent == 's'):
        return True


print(play())
