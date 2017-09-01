"""

A simple guess the number game made with randint in python

"""

from random import randint

class Number(object):

    def __init__(self):

        self.min = None
        self.max = None
        self.cont = True

        checkFlag = [False, False]

        while not all(checkFlag):
            try:
                if self.min == None:
                    self.min = int(input("Please enter the minimum number: "))
                    checkFlag[0] = True
                if self.max == None:
                    self.max = int(input("Please enter the maximum number: "))
                    checkFlag[1] = True
                if(all(checkFlag) and self.min > self.max):
                    print("Please enter the minimum and maximum values correctly!")
                    self.min = None
                    self.max = None
                    checkFlag[0] = False
                    checkFlag[1] = False
            except ValueError:
                print("Please enter a valid input!")

    def getRandomNumber(self):

        self.correctAnswer = randint(self.min, self.max)

    def getInput(self):

        check = False
        guessCount = 1

        while not check:
            try:
                guess = input("Please enter your guess(exit to exit): ")

                guess = int(guess)

                if guess == "exit":
                    self.cont = False
                    break

                if guess < self.min or guess > self.max:
                    print("Please enter your guess between the limits!", self.min, "to", self.max)
                    continue
                elif guess == self.correctAnswer:
                    print("You've guessed correctly! Number of guesses: %d" % guessCount)
                    check = True
                else:
                    if guess < self.correctAnswer:
                        print("The answer is bigger!")
                        continue
                    else:
                        print("The answer is smaller!")
                guessCount += 1
            except ValueError:
                print("Please enter a valid input!")

    def toContinue(self):

        if not self.cont:
            return False

        while True:

            checkContinue = input("Do you want to continue? Y/n\n")
            if checkContinue == 'Y' or checkContinue == 'y':
                return True
            elif checkContinue == 'N' or checkContinue == 'n':
                return False
            else:
                print("Please enter a valid input!")



flag = True

while flag:
    guessNumber = Number()
    guessNumber.getRandomNumber()
    guessNumber.getInput()
    flag = guessNumber.toContinue()