import random
print("Welcome to my game")
word_list = ("tungsten", "mercury", "hydrogen")
print("you get 5 guesses")
secret_word = random.choice(word_list)
empty_list = []
for letter in secret_word:
    empty_list += "_"
num = 0
game_over = False
while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            empty_list[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"you have {guesses_left} guesses_left")
        if num >= 5:
            print("you loose")
            game_over = True
    print(empty_list)
    if "_" not in empty_list:
        print("you win")
        game_over = True
