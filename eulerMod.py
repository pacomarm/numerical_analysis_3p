def f(t,y):
    return y - (t**2) + 1

def t(h,i): 
    return h*i

def eulerMod(N, a, b,alpha):
    w = []
    h = (b-a)/N
    for i in range(11):
        if(i==0):
            w.append(alpha)
        else: 
            temp = w[i-1] + (h)/2 * ( f(t(h,i-1), w[i-1]) + f( t(h,i), w[i-1] + h*f(t(h,i-1), w[i-1])))
            w.append(temp) 
    return w
    

