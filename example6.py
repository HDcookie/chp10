path = ''
filename = 'journal.txt'
with open(path + filename, 'w') as file_object:
    while True:
        line = input(':')
        if line == '#quit':
            break
        else:
            file_object.write(line + '\n')
        
        
