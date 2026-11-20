names = []

name = input("Name (done to stop): ")

counter = 0

while name != "done":
    names.append(name)
    counter = counter + 1
    name = input("Name (done to stop): ")
    
print(names)
print(f"{counter} name stored")
    

