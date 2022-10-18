# Appending to a File
'''
    If you don't want to erase content in a previously written file, you can use
    the append feature to add on new text to the end of the file.
'''
path = '\\\\Mac\\Home\Documents\\projects\\chp10\\'
filename = 'journal.txt'
with open(path + filename, 'a') as file_object:
    while True:
        line = input(':')
        if line == '#quit':
            file_object.write('-'*80)
            break
        else:
            file_object.write(line + '\n')
        
        
