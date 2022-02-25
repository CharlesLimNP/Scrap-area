def add(*numbers):
    """
    Compute the sum of all numbers supplied that are separated by a comma
    """
    number = 0
    for num in numbers:
        number += num
    return number