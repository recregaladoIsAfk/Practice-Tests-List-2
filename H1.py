members = []

member = input("Member (or done): ")

while member != "done":
    members.append(member)
    member = input("Member (or done): ")
  
    
target = input("Look for: ")

def find(members, target):
    for i in range(len(members)):
        if members[i] == target:
            return (f"{target} is member number {i+1}")

    return (f"{target} is not a member")
    
print(find(members, target))

