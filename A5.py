names = []  

for i in range(5):
    name = input("Name: ")
    names.append(name)

target = input("Looking for: ")

found = False

for i in range(5):
    if names[i] == target:
        found = True
    
if found == True:
    print(f"{target} is in the list")
    
else:
    print(f"{target} is not in the list")
    