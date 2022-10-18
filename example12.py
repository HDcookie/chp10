# Handling the FileNotFoundError Exception
path = '\\\\Mac\\Home\\Documents\\projects\\chp10\\'

filename = input('Enter the file path and name: ')
try:
    with open(path + filename, encoding='utf-8') as f:
        contents = f.read()
except:
    print(f'Sorry. the file {filename} could not be found.')
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_of_words = len(words)
    print(f'The book {filename} has about {num_of_words} words.')
    

    

        
        