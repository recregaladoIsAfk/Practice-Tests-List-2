Total = 0
for i in range(5):
    score = int(input("Score: "))
    if score >= 75:
        Total = Total + 1
    
print(f"{Total} of 5 passed")
