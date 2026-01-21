import json 

with open("./data/users.json", "rw") as users_file:
    users = json.load(users_file)

print(users)