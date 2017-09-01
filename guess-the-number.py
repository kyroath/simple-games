"""

A simple guess the number game made with randint in python

"""

from random import randint


class Number(object):
    def __init__(self):

        self.min = None
        self.max = None
        self.cont = True

        check_flag = [False, False]

        while not all(check_flag):
            try:
                if self.min is None:
                    self.min = int(input("Please enter the minimum number: "))
                    check_flag[0] = True
                if self.max is None:
                    self.max = int(input("Please enter the maximum number: "))
                    check_flag[1] = True
                if all(check_flag) and self.min > self.max:
                    print("Please enter the minimum and maximum values correctly!")
                    self.min = None
                    self.max = None
                    check_flag[0] = False
                    check_flag[1] = False
            except ValueError:
                print("Please enter a valid input!")

        self.correctAnswer = randint(self.min, self.max)

    def getInput(self):

        check = False
        guess_count = 0

        while not check:
            try:
                guess = input("Please enter your guess(exit to exit): ")
                guess = int(guess)

                guess_count += 1

                if guess == "exit":
                    self.cont = False
                    break

                if guess < self.min or guess > self.max:
                    print("Please enter your guess between the limits!", self.min, "to", self.max)
                    continue
                elif guess == self.correctAnswer:
                    print("You've guessed correctly! Number of guesses: %d" % guess_count)
                    check = True
                else:
                    if guess < self.correctAnswer:
                        print("The answer is bigger!")
                        continue
                    else:
                        print("The answer is smaller!")
            except ValueError:
                print("Please enter a valid input!")

    def toContinue(self):

        if not self.cont:
            return False

        while True:

            check_continue = input("Do you want to continue? Y/n\n")
            if check_continue == 'Y' or check_continue == 'y':
                return True
            elif check_continue == 'N' or check_continue == 'n':
                return False
            else:
                print("Please enter a valid input!")


flag = True

while flag:
    guessNumber = Number()
    guessNumber.getInput()
    flag = guessNumber.toContinue()
