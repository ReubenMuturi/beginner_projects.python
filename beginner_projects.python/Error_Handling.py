
def safe_divide(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "Cannot divide by Zero"
    except TypeError:
        return "both numbers must be inputs"
#
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# print(safe_divide(10, "two"))


def calculate_mean(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return "The list is empty; cannot compute mean."
    except TypeError:
        return "The list contain only  numbers."

print(calculate_mean([1,2,3,4,5,6,7]))
print(calculate_mean([]))
print([1,2,3,"four",5])