message = "Hello zorld"
number = 3
display = ""
letters = "abcdefghijklmnopqrstuvwxyz"


for letter in message.lower():
    x = letters.find(letter)
    convert = (x + number) % len(letters)
    new_word = letters[convert]
    for x in new_word:
        display += x
for letter in message.lower():
    if letter == " ":
        p = message.find(" ")
        v = display.find("c")

        print(display)
        print(f"initial message:" + message)
        print(f"final message:", display)
        break
