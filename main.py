def add(x, y):
    '''
    Returns the sum of two user input numbers.
    '''
    return x + y

def subtract(x, y):
    '''
    Returns the difference between two user input numbers.
    '''
    return x - y

def multiply(x, y):
    '''
    Returns the product of two user input numbers.
    '''
    return x * y

def divide(x, y):
    '''
    Returns the quotient when one of two user input numbers is divided by the other.
    '''
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")