from random import choice
choices = ['R', 'P', 'S']


def game(player, computer):
    if set([player, computer]) == set(['R', 'S']):
        if player == 'R':
            return True
        else:
            return False
    elif set([player, computer]) == set(['P', 'R']):
        if player == 'P':
            return True
        else:
            return False
    elif set([player, computer]) == set(['S', 'P']):
        if player == 'S':
            return True
        else:
            return False
    else:
        return 'draw'


def move_names(player, computer):
    picked_moves = []
    for choice in [player, computer]:
        if choice == 'R':
            picked_moves.append('Rock')
        elif choice == 'P':
            picked_moves.append('Paper')
        else:
            picked_moves.append('Scissors')

    return picked_moves


print('Rock paper Scissors Game')
print('You\'re playing against the computer')
won = False

while won == False:
    print('pick an option:\nR: Rock\nP: Paper\nS: Scissors')
    option = input()
    if option in choices:
        computer = choice(choices)
        moves = move_names(option, computer)
        print(f'Player ({moves[0]}) : CPU ({moves[1]})')
        won = game(option, computer)
        if won == 'draw':
            won = False
            print('\n')
        elif won == True:
            print('Winner: Player')
            break
        elif won == False:
            print('Winner: CPU')
            break
    else:
        print('Invalid option!\n\n')
