def addition(num_a, num_b):
    """
    Add two numbers together
    """
    return num_a + num_b
def subtraction(num_a, num_b):
    """
    Subtract two numbers
    """
    return num_a - num_b
def division(num_a, num_b):
    """
    divide two numbers
    """
    return num_a / num_b
def multiplcation(num_a, num_b):
    """
    multiply two numbers
    """
    return num_a * num_b

def main():
    while True:
        num_a = input('Enter a number:')
        if num_a == 'q':
            return
        while True:
            try:
                num_a = int(num_a)
                return num_a
            except:
                print('Invalid input')
                
        operand = input('enter an operand: ')
        if operand == 'q':
            return
        num_b = input('Enter another number: ')
