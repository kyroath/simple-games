import random

words = {
    "colors": ["aquamarine", "thistle", "blue", "cyan", "magenta", "pine green", "white", "yellow", "grey", "black", "melon"],
    "astronomy": ["star", "planet", "nasa", "telescope", "shuttle", "starquake", "sun", "exoplanet"],
    "weather": ["drizzle", "showers", "hail", "sleet", "hot", "warm", "breeze", "cold", "hurricane", "blizzard", "cloudy", "foggy", "overcast"],
    "movies": ["the godfather", "shawshank redemption", "the dark knight", "pulp fiction", "fight club", "inception"]
}

answer = []


def printQuestion(word):
    count = 0
    for i in word:
        if answer[count]:
            print(i, end='')
            count += 1
            continue
        if i == ' ':
            count += 1
            print(i, end='')
        else:
            count += 1
            print('_', end='')
    print()


def checkUsed(letter):
    for i in used_letters:
        if i == letter:
            return True
    return False


def checkIfIn(letter):
    count = 0
    flag = False
    for i in secret_word:
        if i == letter:
            answer[count] = True
            flag = True
        count += 1
    if flag:
        return True
    return False


def printList(lists):

    if len(lists) == 0:
        print("Empty.")
        return

    for i in lists:
        print(i, end=' ')
    print()

while True:
    try:
        print("Topics:")
        printList(list(words))
        topic = input("Please choose a topic: ")

        secret_word = random.choice(words[topic])

        break
    except KeyError:
        print("Please enter a valid topic!")


for i in range(len(secret_word)):
    answer.append(False)

life = 7
used_letters = []

while life > 0:

    if all(answer):
        print("You Win!")
        break

    printQuestion(secret_word)
    printList(used_letters)

    input_letter = input("Please enter an unused letter:")

    if not input_letter.isalpha() or checkUsed(input_letter) or not len(input_letter) == 1:
        continue

    used_letters.append(input_letter)

    if checkIfIn(input_letter):
        continue

    life -= 1
    print("You guessed wrong! Remaining guesses:", life)

print("The secret word is:", secret_word, end='')