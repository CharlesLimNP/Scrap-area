def add(*numbers):
    """
    Computes the sum of all numbers supplied that are separated by a comma
    """
    number = 0
    for num in numbers:
        number += num
    return number

def print_underline(words):
    """
    print the words supplied and add asterisks as an underline
    """
    print(words)
    print("*" * len(words))