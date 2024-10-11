def largest_range(array):
    # Store the numbers in a set for O(1) access
    numbers = set(array)
    best_range = []
    longest_length = 0

    for number in array:
        if number not in numbers:
            continue

        # Remove the number from the set to avoid duplicate processing
        numbers.remove(number)

        current_length = 1
        left = number - 1
        right = number + 1

        # Expand to the left of the current number
        while left in numbers:
            numbers.remove(left)
            current_length += 1
            left -= 1

        # Expand to the right of the current number
        while right in numbers:
            numbers.remove(right)
            current_length += 1
            right += 1

        # Update the best range if the current range is longer
        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]


    return best_range


# Example usage
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largest_range(array))  # Output: [0, 7]