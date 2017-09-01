""""

This program simulates a dice throw using randint, and it is possible to change the number of sides the dice has

"""

import random


class Dice(object):

    def __init__(self, dice_side):
        self.side = int(dice_side)

    def throw(self):
        print("The result is:", random.randint(1, self.side))

    def changeSide(self, dice_side):
        self.side = dice_side

flag = True

while flag:
    try:
        side = int(input("Enter the number of sides: "))
        dice = Dice(side)
        dice.throw()

    except ValueError:
        print("Enter a valid input!")
        continue

    finally:
        while True:
            answer = input("Do you want to continue? Y/n\n")
            if answer == 'Y' or answer == 'y':
                break
            elif answer == 'N' or answer == 'n':
                flag = False
                break
            else:
                print("Enter a valid input!")
