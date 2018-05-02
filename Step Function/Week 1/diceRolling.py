import random

play_game = True

while play_game:
    roll_dice = input('Want to roll the dice? Answer with Y/N: ')
    if (roll_dice == 'Y') or (roll_dice == 'y'):
        number = random.randrange(1,7)
        print('The number the dice landed on is {0}'.format(number))
    elif (roll_dice == 'N') or (roll_dice == 'n'):
        play_game = False
    else:
        print('Only accepeted answer is Y/N')
print('See you soon')
