# open & close

# file = open('./data/users.txt', 'w')
# file = open('./data/users.txt', 'a')

# file.write("Hola Daniel \n")
# file.write("Python Mola\n")
# file.close()

with open('./data/users.md', 'a') as file:
    file.write(f"# {input("introduce un texto: ")}")