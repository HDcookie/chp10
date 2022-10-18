# Large File: One Million Digits
filename = 'pi_digits_million.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input('Enter your birthday, in the format mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
    print(f'index: {pi_string.index(birthday)}')
else:
    print('Sorry... Your birthday was not found in the first million digits of pi.')

