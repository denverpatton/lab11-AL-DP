import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # According to your requirement: division is b / a
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm undefined for non-positive inputs.")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1.")

    return math.log(b) / math.log(a)

def exp(a, b):
    # a^b
    return a ** b
