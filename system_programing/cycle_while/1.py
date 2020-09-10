total = 100
while total > 0:
    n = int(input("n = "))
    if total < n:
        print("больше чем ", total)
    else:
        total -= n

print(total)