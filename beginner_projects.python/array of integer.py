# Write a function that takes an array of integers and return an array af length 2 representing the largest range
# of numbers contained in the array.
# The first number in the output array should be the first number in the range while the second number should be
# the last number in the range.
# A range of numbers is defined as a set of numbers that came right after each other in the set of real integers.
# For instance, the output array[2,6] represents the range{2,3,4,5,6}, which is a range of length 5.
# Note that numbers do not need to be ordered or adjacent in the array in order to form a range.
# Assume that there will only be one largest range.
# Sample input:[1,11,3,0,15,5,2,4,10,7,12,6]
# Sample output:[0,7]

# Writing code
def largestrange(array):
    numbers = {x: 0 for x in array}  # create a hash table
    left = right = 0  # To keep track of longest sequence
    for left_count in numbers:
        left_count = array = -1

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

        # Go as far left and right as possible

        while left_count in numbers:  # 0(1)
            # Eg number 4, left_count = 3 if 3 is in numbers then +1
            numbers[left_count] = 1
            # while left_count of 3 (2) is not present then -1
            left_count -= 1
            # Since only 3 was in our left_count then left_count of 4 = +1
        left_count + 1

        while right_count in numbers:
            numbers[right_count] = 1
            right_count += 1
        right_count -= 1

        if (right-left) <= (right_count-left_count):
            right = right_count
            left = left_count

            return (left, right)
