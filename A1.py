items = []

for i in range(4):
    item = input("Item: ")
    items.append(item)
    
for i in range(len(items)):
    print(i + 1, items[i])
