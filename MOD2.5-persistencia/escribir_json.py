import json

users = [
    {
        "id":1,
        "nombre":"Juan José"
    },
    {
        "id":2,
        "nombre":"Antonio"
    },
    {
        "id":3,
        "nombre":"Juan Antonio"
    },
]

# Opción 1 (mala)
users_json = json.dumps(users)
print(users_json)

with open('./data/users.json', 'a') as file:
    file.write(users_json)

# Opción 2: Directa

with open("./data/users.json", "w") as users_file:
    json.dump(users, users_file, indent=4)