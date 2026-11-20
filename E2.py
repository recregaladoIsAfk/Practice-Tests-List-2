names = []

num = int(input("How many names?: "))
for counter in range(num):
    name = input("Names: ")
    names.append(name)
    
print(names)
print(num, 'Names stored')
