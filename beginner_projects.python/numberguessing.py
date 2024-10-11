import random
answer = input("Guess a number (YOU ONLY HAVE 5 TRIALS :)) ")
if answer.isdigit():
    answer = int(answer)
    rand = random.randint(0, 10)
    print(rand)
if answer >= 11:
    print("guess a number in the range -1 - 11")
guesses = 0
while True:
    guesses += 1
    if guesses == 10:
        quit()
    print("you have", int(5 - guesses), "guesses left")

    answer = input("Guess a number ")
    if answer.isdigit():
        answer = int(answer)
        rand = random.randint(0, 10)
        print(rand)

    if rand == answer:
        print("correct")
        print("you got it in", guesses, "guesses")
        break
    else:
        continue
