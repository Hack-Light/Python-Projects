import random


def play():

    print('Welcome to our almighty rock-paper-scissors game')

    user = input(
        "What's your choice? r for rock, p for paper, s for scissors: ")

    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        print('It is a tie')
        return

    if is_win(user, computer):
        print("You won")
        return

    print("You lost")
    return


def is_win(player, opponent):
    if (player == 'r' and opponent == "s") or (player == 's' and opponent == "p") or (player == 'p' and opponent == 'r'):
        return True


play()
