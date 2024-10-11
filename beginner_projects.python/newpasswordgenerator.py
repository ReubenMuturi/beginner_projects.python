import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special_characters = "!@#$%^&*()_-';<>?"
numbers = "0123456789"
i = 0
length = int(input("How long do you need your password to be? "))


combined = upper_case + special_characters + numbers + lower_case
display = ""
print("Password: ", end='')

while i < length:
    rand = random.choice(combined)
    display = rand
    print(display, end='')
    i += 1

