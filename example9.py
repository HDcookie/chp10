# Handling ZeroDivision Error Exception
number = input('Input a number and we will try to divide by zero: ')
try:
    number = float(number)
    print(number / 0)
except:
    print('Division by zero is not allowed.')
    
    