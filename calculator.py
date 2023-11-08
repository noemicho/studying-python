def sum(num1, num2):
    sumN = num1+num2
    return sumN

def sub(num1, num2):
    subN = num1 - num2
    return subN
    
def div(num1, num2):
    divN = num1 / num2
    return divN
    
def mult(num1, num2):
    multN = num1 * num2
    return multN
    
def defineOp(op, number1, number2):
    if op == '+':
        result = sum(number1,number2)
        print('RESULT: ', result)
        return result
    elif op == '-':
        result = sub(number1, number2)
        print('RESULT: ', result)
        return result
    elif op == '/':
        result = div(number1, number2)
        print('RESULT: ', result)
        return result
    elif op == '*':
        result = mult(number1, number2)
        print('RESULT: ', result)
        return result
    else:
        print('Operation not valid')
    
    
def calculator():
    print('******** CALCULATOR *********\n \n')
    while True:
        number1 = float(input('NUMBER: '))
        op = input('OPERATION: ')
        number2 = float(input('NUMBER: '))
        defineOp(op, number1, number2)
        print('\n___________\n')


calculator()