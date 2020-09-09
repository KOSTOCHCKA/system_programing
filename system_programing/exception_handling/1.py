import time
try:
	a = input()
	b = input()
	print(int(a) + int(b))
except ValueError:
	print(a + b)

time.sleep(2)