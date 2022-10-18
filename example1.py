filename = 'chp10/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        # Notice it prints out empty lines. How do we fix this?