memory = []
memory2 = []

def addition(var1,var2):
    appender = memory.append(var1+var2)
    return var1+var2
def subtraction(var1,var2):
    appender = memory.append(var1-var2)
    return var1-var2
def multiplication(var1,var2):
    appender = memory.append(var1*var2)
    return var1*var2
def division(var1,var2):    
    if var2 == 0:
        return 'Error: Division by zero is not allowed'
    appender = memory.append(var1/var2)
    return var1/var2

def num_receiver():
    converting = True
    while converting:
        var = input('Enter a number: ')
        try:
            var = int(var)
            return var
        except ValueError:
            print('Invalid input')
            continue

def operand_receiver():
    analysing = True
    valid_operands = {'+','-','*','/'}
    while analysing:
        operand = input('Enter an operand(+,-,*,/): ')
        if operand in valid_operands:
            return operand
        else:
            print('Invalid input')
            continue

def main():
    for i in range(12):
        var1 = num_receiver()
        operand = operand_receiver()
        var2 = num_receiver()
        operand2 = operand_receiver()
        if operand == '-':
            print(subtraction(var1,var2))

        elif operand == '+':
            print(addition(var1,var2))

        elif operand == '/':
            print(division(var1,var2))

        elif operand == '*':
            print(multiplication(var1,var2))

        else:
            print('Invalid input')
        

if __name__ == '__main__':
    main()