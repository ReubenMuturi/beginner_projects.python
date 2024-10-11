numbers = int(0)

p = input("Give 20 random numbers between 1 - 20  ")
array1 = numbers


def longestrange(arr):

    var: p = {x: 0 for x in arr}
    print("Welcome to range")


left_count = 0
right_count = 0
left = right = 0

if numbers != 20:
    print("You need to type in a min 20 digits")

for number in p:
    if number == 0:
        left_count = -1
    right_count = +1

    while left_count in numbers:  # 0(1)
        # Eg number 4, left_count = 3 if 3 is in numbers then +1
        numbers[left_count] = 1
        # while left_count of 3 (2) is not present then -1
        left_count -= 1
        # Since only 3 was in our left_count then left_count of 4 = +1

    while right_count in numbers:
        right_count = 1
        right_count += 1
    right_count -= 1

    if (right - left) <= (right_count - left_count):
        right = right_count
        left = left_count

    print(right_count, left_count)
