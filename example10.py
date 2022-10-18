print('Enter two numbers and I will try to divide them.')
print('Enter \'q\' to quit.')

while True:
    number1 = input('number1: ')
    if number1 == 'q':
        break
    
    number2 = input('number2: ')
    if number2 == 'q':
        break
    
    try:
        answer = float(number1) / float(number2)
        print(answer)
    except ZeroDivisionError:
        print('You can\'t divide by zero!')
    except ValueError:
        print('You must enter a number!')
    
    