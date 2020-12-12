import matplotlib.pyplot as plt

x = []
w = []

def f(t,y):
  return y-(t**2)+1;

def runge_kutta_order4(N, a, b, alpha):
    h = (b-a)/N
    ts = [a]
    ws = [alpha]
    t_i = a
    w_i = alpha
    for i in range(N):
        t_i = t_i + h
        k_1 = h*f(t_i,w_i)
        k_2 = h*f(t_i+(h/2),w_i+(0.5*k_1))
        k_3 = h*f(t_i+(h/2),w_i+(0.5*k_2))
        k_4 = h*f(t_i+h,w_i+k_3)
        w_i = w_i+(1/6)*(k_1+2*k_2+2*k_3+k_4)
        ts.append(t_i)
        ws.append(w_i)
    return ts, ws

x, w = runge_kutta_order4(10, 0.0, 2.0, .5);

print(x,w)

plt.plot(x, w,'red', label='function')
plt.title('Runge-Kutta-N=4')
plt.show() 
