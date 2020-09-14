import time

def function():
    a = int(input())
    b = a
    while a != 0:
        a = int(input())
        if a == 0:
            break
        c = a * b
        b = c
    return b
 
print(function())

time.sleep(2)