import time
def test():
    x = int(input())
    if x > 0:
        positive()
    elif x == 0:
    	nul()
    else:
        negative()
 
def positive():
    print('Положительное')
 
def negative():
    print('Отрицательное')
    
def nul():
	print('ноль это ноль')

test()
time.sleep(2)