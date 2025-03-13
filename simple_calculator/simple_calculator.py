import operations as op
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
    var1 = num_receiver()
    operand = operand_receiver()
    var2 = num_receiver()
    if operand == '-':
        print(op.subtraction(var1,var2))

    elif operand == '+':
        print(op.addition(var1,var2))

    elif operand == '/':
        print(op.division(var1,var2))

    elif operand == '*':
        print(op.multiplication(var1,var2))

    else:
        print('Invalid input')

if __name__ == '__main__':
    main()