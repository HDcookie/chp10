filename = 'chp10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # now we have a list called 'lines'. The list contains all the lines in our
    # file_object
    
for line in lines:
    print(line.rstrip())