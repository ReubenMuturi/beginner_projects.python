import random

code = "pythonx"
alphabets = "abcdefghijklmnopqrstuvwxyz"
new_password = []
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def password_generator():
    x = 0
    while x < 7:
        new_index = " "
        rando = " "
        number = (alphabets.find(code[x]))
        rand = random.choice(numbers)
        rando += str(rand)

        if round(number + rand) > 26:
            new = alphabets[round((number + rand)/26)]
            new_index += str(new)
        x += 1
        print(new_index)


password_generator()
