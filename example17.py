import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}")
    
# Now let's go to page 205 and modify this even further...