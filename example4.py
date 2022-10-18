# Large File: One Million Digits
filename = 'chp10/pi_digits_million.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:53]}")
print(len(pi_string))

