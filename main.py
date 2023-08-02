def add(x: float, y: float) -> float:
    '''
    Takes in two numbers x and y and returns the sum of the two numbers.
    '''
    return x + y

def subtract(x: float, y: float) -> float:
    '''
    Takes in two numbers x and y and returns the difference between the two numbers.
    '''
    return x - y

def multiply(x: float, y: float) -> float:
    '''
    Takes in two numbers x and y and returns the product of the two numbers.
    '''
    return x * y

def divide(x: float, y: float) -> float:
    '''
    Takes in two numbers x and y and returns the quotient when x is divided by y.
    '''
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")