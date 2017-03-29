import matplotlib.pyplot as pyplot


class Graph:

	def f(x):
		return x

	def __init__(self, func = f):
		self.func = func 

	def plot(self):

		x = range(10) 
		y = []
		
		for i in x:
			y.append(self.func(i))
		pyplot.plot(x,y)
		pyplot.show()

