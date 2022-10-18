# Handling the FileNotFoundError Exception
path = ''

filename = input('Enter the file path and name: ')
with open(path + filename, encoding='utf-8') as f:
    lines = f.readlines()
    
while True:
    print(f'Max Line Number: {len(lines)}')
    line_num = input('Enter the line number: ')
    if line_num == 'q':
        break
    else:
        print(lines[int(line_num)-1])
        
        