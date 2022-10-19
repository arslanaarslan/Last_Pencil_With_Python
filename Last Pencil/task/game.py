import random

names = ["Jack", "John"]
penToDecrease = ['1', '2', '3']


def is_digit(number_of_pencils):  # Check if the input numeric or not
    while not number_of_pencils.isdigit():
        print("The number of pencils should be numeric")
        number_of_pencils = input()
    return int(number_of_pencils)


def is_digit_and_positive(number_of_pencils):  # Check if the input is digiy and positive or not
    number_of_pencils = is_digit(number_of_pencils)
    while not number_of_pencils > 0:
        print("The number of pencils should be positive")
        number_of_pencils = input()
        number_of_pencils = is_digit(number_of_pencils)
    return number_of_pencils


def check_name(bot_player):  # Check if the username is correct
    while bot_player not in names:
        print("Choose between John and Jack")
        bot_player = input()
    return bot_player


def is_in_the_range(number_to_decrease):
    while number_to_decrease not in penToDecrease:
        print("Possible values:'1', '2' or '3'")
        number_to_decrease = input()
    return int(number_to_decrease)


def decrease_number():
    if player == 1:
        if numberOfPencils % 4 == 0:
            number_to_decrease = 3
        elif numberOfPencils % 4 == 3:
            number_to_decrease = 2
        else:
            number_to_decrease = 1

        print(number_to_decrease)
    else:
        number_to_decrease = is_in_the_range(input())

    return number_to_decrease


print("How many pencils would you like to use:")

numberOfPencils = input()
numberOfPencils = is_digit_and_positive(numberOfPencils)

print("Who will be the first (John, Jack):")

player_name = input()
player_name = check_name(player_name)  # If player==1 Jack is bot
# If player==-1 John is bot
if player_name == names[0]:
    player = 1
else:
    player = -1

print("|" * numberOfPencils)

while numberOfPencils > 0:
    if player == 1:
        print("Jack's turn:")
    else:
        print("John's turn:")

    numberToDecrease = decrease_number()

    while numberToDecrease > numberOfPencils:
        print('Too many pencils were taken')
        numberToDecrease = decrease_number()

    numberOfPencils -= numberToDecrease
    if numberOfPencils != 0:
        print('|' * numberOfPencils)

    player *= -1

if player == 1:
    print("Jack won!")
else:
    print("John won!")
