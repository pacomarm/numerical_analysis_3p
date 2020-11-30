def w_next(w, i):
    return w + .2*(w-.04*(i**2)+1+(.2/2)*(w-.04*(i**2)-.4*i+1) + (.2**2)/(6)*(w-.04*(i**2)-.4*i-1)+ (.2**3)/(24)*(w-.04*(i**2)-.4*i-1))

ws = []
w = []
for i in range(11):
    print(i)
    if(i == 0):
        ws.append(.5)
        w.append(.5)
        pass
    else:
        ws.append(round(w_next(ws[i-1],i-1), 5))
        w.append(w_next(ws[i-1],i-1))
# print(ws)
print(w)