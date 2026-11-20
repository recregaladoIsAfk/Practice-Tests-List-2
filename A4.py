scores = []

for i in range(5):
    score = int(input("Score: "))
    scores.append(score)
    highest = scores[0]
    if score > highest:
        highest = score
        

print(f"Highest: {highest}")
