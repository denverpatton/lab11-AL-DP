#https://github.com/denverpatton/lab11-AL-DP.git
#Partner 1: Allen Lin
#Partner 2: Denver Patton

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Square root cannot be negative")
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # According to your requirement: division is b / a
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm undefined for non-positive inputs.")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1.")

    return math.log(b) / math.log(a)

def exp(a, b):
    # a^b
    return a ** b
