filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # now we have a list called 'lines'. The list contains all the lines in our
    # file_object
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))