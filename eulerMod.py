import matplotlib.pyplot as plt

x = []
w = []

def f(t,y):
    return y - (t**2) + 1

def t(h,i): 
    return h*i

def eulerMod(N, a, b,alpha):
    h = (b-a)/N
    for i in range(11):
        x.append( a + t(h,i))
        if(i==0):
            w.append(alpha)
        else: 
            temp = w[i-1] + (h)/2 * ( f(t(h,i-1), w[i-1]) + f( t(h,i), w[i-1] + h*f(t(h,i-1), w[i-1])))
            w.append(temp) 
    return w

eulerMod(10, 0.0, 2.0, .5)

plt.plot(x, w,'red', label='funcion')
plt.title('Euler Mod')
plt.legend()
plt.show()   

