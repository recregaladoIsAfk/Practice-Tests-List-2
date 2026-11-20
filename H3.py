votes = []

vote = input("Vote (done to stop): ")

while vote != "done":
    votes.append(vote)
    vote = input("Vote (done to stop): ")
    
target = input("Candidate: ")

counter = []
def count(items, target):
    for i in range(len(votes)):
        if votes[i] == target:
            counter.append(i)
    return (f"{target} got {len(counter)} vote(s)")
            
print(count(votes, target))
        
    