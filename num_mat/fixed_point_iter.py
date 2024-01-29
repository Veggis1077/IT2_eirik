import numpy as np
import matplotlib.pyplot as plt

def fpi(func, x0, n):
    xn = x0
    for i in range(n):
        xn = func(xn)
    return xn

def func1(x):
    return 1+ (1/4) * np.sin(x)


print(fpi(func1, 1, 10))

X=np.linspace(5,5,100)
Y=f(X)
dY=df(X,0.01) # 0.01 = delta-x
d2Y=d2f(X,0.01)
drealY=realdf(X)

plt.plot(X,Y)
plt.plot(X,dY)
plt.plot(X,d2Y)
plt.plot(X,drealY)
plt.grid()
plt.legend()
plt.show()