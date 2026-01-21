
# open & close

# file = open('./data/users.txt', 'r')
# content = file.read()
# file.close()
# print(content)


with open('./data/users.md', 'r') as file:
    content = file.read()
print(content)