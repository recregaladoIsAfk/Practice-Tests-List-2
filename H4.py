votes = []

vote = input("Vote (done to stop): ")

while vote != "done":
    votes.append(vote)
    vote = input("Vote (done to stop): ")
    
target = input("Candidate: ")
counter = []

def find_all(items, target):
    for i in range(len(votes)):
        if votes[i] == target:
            counter.append(i)
    return (f"{target} is at positions {counter}")
            
print(find_all(votes, target))
        
    