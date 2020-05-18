def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    return str(max(numbers)) + ' ' + str(min(numbers))