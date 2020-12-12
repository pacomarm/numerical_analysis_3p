# alpha = 0.5
# a = 0
# b = 2
# N = 100
# h = (b-a)/N

import matplotlib.pyplot as plt

x = []
w = []

def f(t,y):
  return y-(t**2)+1;

def runge_kutta_midpoint(N, a, b, alpha):
    h = (b-a)/N
    ts = [a]
    ws = [alpha]
    t_i = a
    w_i = alpha
    for i in range(N):
        t_i = t_i + h
        w_i = w_i+h*f(t_i+(h/2),w_i+(h/2)*f(t_i,w_i))
        ts.append(t_i)
        ws.append(w_i)
    return ts, ws

x, w = runge_kutta_midpoint(10, 0.0, 2.0, .5);

plt.plot(x, w,'red', label='function')
plt.title('Runge-Kutta-Mid')
plt.show()  



