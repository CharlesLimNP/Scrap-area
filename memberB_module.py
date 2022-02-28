def evenOrOdd(number):
    """
    Takes an integer and determine if it is an odd or even number. Returns string "odd" or "even"
    """ 
    if (number % 2) == 0:
        return "even"
    else:
        return "odd"

def fib(n):
    """
    Takes an integer, computes the Fibonacci sequence and returns an iterator object.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
