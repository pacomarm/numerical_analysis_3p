def f(t,y):
    return y - (t**2) + 1

def t(h,i):
    return h*i

def euler( N, a, b, alpha):
    h = (b - a)/N
    w = []
    for i in range(N+1):
        if i == 0:
            w.append(alpha)
        else:
            next = w[i-1] + h*f( t(h,i-1), w[i-1])
            w.append(next)
    return w
