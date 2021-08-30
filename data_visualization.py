import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

def plot_a(a, x0):
	x = np.array([])
	for i in range(0,101,1):
		x = np.append(x, i/100)

	graph = plt.figure()
	graph = graph.add_subplot(111)

	graph.minorticks_on()
	graph.set_xlabel('N(t)')
	graph.set_ylabel('N(t+1)')
	graph.grid(which='minor', alpha=0.5)
	graph.grid(which='major', alpha=0.5)

	graph.plot(x, x, alpha=0.5)
	graph.plot(x, a*x*(1-x))

	cx, cy = np.empty((2,41,2))
	cx[0] = x0
	cy[0] = 0
	for n in range(1, 40, 2):
		cx[n] = cx[n-1]
		cy[n] = a*cx[n-1]*(1-cx[n-1])
		cy[n+1] = cy[n]
		cx[n+1] = cy[n]

	graph.plot(cx, cy, alpha=0.5)

	plt.show()

def plot_b(a):
	graph = plt.figure()
	graph = graph.add_subplot(111)

	graph.set_xlabel('t')
	graph.set_ylabel('N(t+1)')
	graph.grid(which='minor', alpha=0.5)
	graph.grid(which='major', alpha=0.5)

	y = [0 for i in range(100)]
	x = [i for i in range(100)]
	y[0] = 10**(-5)

	for i in range(1, 100, 1):
		y[i] = a*y[i-1]*(1-y[i-1])

	graph.plot(x,y)
	plt.show()


def plot_c():
	graph = plt.figure()
	graph = graph.add_subplot(111)

	graph.set_xlabel('a')
	graph.set_ylabel('N(t)')
	graph.grid(which='minor', alpha=0.5)
	graph.grid(which='major', alpha=0.5)

	a = np.arange(1.4, 4, 0.01)
	N = 10**(-5)

	for i in range(260):
		N = a*N*(1-N)
		graph.plot(a, N, alpha=0.01)

	plt.show()


# (a)
plot_a(0.5, 0.2)
plot_a(-0.5, 0.2)
plot_a(-1.5, 0.2)

plot_a(1.5, 0.2)
plot_a(2.5, 0.2)
plot_a(3.5, 0.2)

# (b)
plot_b(0.5)
plot_b(-0.5)
plot_b(-1.5)

plot_b(1.5)
plot_b(2.5)
plot_b(3.5)

# (c)
plot_c()