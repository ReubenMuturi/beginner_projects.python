import random
print("Welcome")
age = input("What is your age? ")
print(age)
for answer in age:
    if int(age) <= 17:
        print("sorry!!")
        quit()
if int(age) >= 18:
    print("Lets play!!")

p = "rock", "paper", "scissors"
rand = random.choice(p)
num = 0
a = input("rock-paper-scissors ")
if a == rand:
    print("retry")
    print(input("rock-paper-scissors? "))

while True:
    for answer in a:
        if rand == "scissors" and a == "paper":
            print(rand)
            print("you loose!!")
            num += 1
            break
        if rand == "scissors" and a == "rock":
            print(rand)
            print("you win!!")
            num += 1
            break
        if rand == "rock" and a == "paper":
            print(rand)
            print("you win!!")
            break
        if rand == "rock" and a == "scissors":
            print(rand)
            print("you loose!!")
            break
        if rand == "paper" and a == "rock":
            print(rand)
            print("you loose!!")
            break
        if rand == "paper" and a == "scissors":
            print(rand)
            print("you win!!")
            break
        if a == "scissors" and rand == "paper":
            print(rand)
            print("I loose!!")
            break
        if a == "scissors" and rand == "rock":
            print(rand)
            print("I win!!")
            break
        if a == "rock" and rand == "paper":
            print(rand)
            print("I win!!")
            break
        if a == "rock" and rand == "scissors":
            print(rand)
            print("I loose!!")
            break
        if a == "paper" and rand == "rock":
            print(rand)
            print("I loose!!")
            break
        if a == "paper" and rand == "scissors":
            print(rand)
            print("I win!!")
            break
    if num == 5:
        print("Good!!")
        break
