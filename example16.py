import json
username = input('what is your username?: ')

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f'We\'ll remember you when you come back, {username}!')