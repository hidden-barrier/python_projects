def multiplication(var0, var2):
    return var0*var2
def division(var0, var2):
    if var2 == 0:
        return 'Error: Divisionby zero is not allowed'
    return var0/var2
def addition(var0, var2):
    return var0+var2
def subtraction(var0,var2):
    return var0-var2
def square(var0):
    return var0*var0
def square_root(var0):
    if var0 < 0:
        return 'Error: Square root of a negative number is not allowed'
    return var0**0.5
def power(var0,var2):
    return pow(var0,var2)
def root(var0,var2):
    if var0 < 0 and var2%2 == 0:
        return 'Error: Root of a negative number is not allowed'
    return pow(var0,1/var2)