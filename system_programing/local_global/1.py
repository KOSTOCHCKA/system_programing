import time
def cylinder():
	try:
		r = float(input('Какой радиус? '))
		h = float(input('Какая высота? '))
		q = int(input('полная площадь - 1, половина - 2 '))
	except ValueError:
		print('Error')
		cylinder()
 
	def circle():
		pl_circle = 3.14 * r ** 2
		return pl_circle
 
 
	if q == 1:
		k = 2 * 3.14 * r * h
		print(k)
	elif q == 2:
		c = (2 * 3.14 * r * h) + (2 * circle())
		print(c)
	else:
		print('Error')
 
 
cylinder()
time.sleep(2)