import matplotlib.pyplot as plt

x = []
w = []

def f(t,y):
    return y - (t**2) + 1

def t(h,i):
    return h*i

def euler( N, a, b, alpha):
    h = (b - a)/N
    for i in range(N+1):
        x.append( a + t(h,i))
        if i == 0:
            w.append(alpha)
        else:
            next = w[i-1] + h*f( t(h,i-1), w[i-1])
            w.append(next)
    return w

euler(10, 0.0, 2.0, .5)

plt.plot(x, w,'red', label='funcion')
plt.title('Euler simple')
plt.legend()
plt.show()