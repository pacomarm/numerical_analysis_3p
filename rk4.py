import matplotlib.pyplot as plt

func = lambda t, y: y - t**2 + 1

def getIntervals(a, b, h):
	while a <= b:
		intervals.append(a)
		a += h

y0 = 0.5
N = 10
a = 0.0
b = 2.0
h = (b-a)/N
intervals = []
weights = []
weights.append(y0)
getIntervals(a, b, h)

def rungeKutta(func, w, t, h):
	k1 = h * func(t,w)
	k2 = h * func(t + h/2, w + k1/2)
	k3 = h * func(t + h/2, w + k2/2)
	k4 = h * func(t + h, w + k3)

	w += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
	return w

for i in range(10):
	w0 = rungeKutta(func, weights[i], intervals[i], h)
	weights.append(w0)

plt.plot(intervals, weights,'red', label='function')
plt.title('Runge-Kutta-N=4')
plt.show() 