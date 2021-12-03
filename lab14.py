from numpy import *
from math import *
import matplotlib.pyplot as plt

def eiler(x, y):
    return x + math.sin(y/sqrt(0.3))
def eiler_koshi(x, y):
    return x + math.cos(y/sqrt(0.3))

def method1(eiler, x, y):
    h = 0.1
    x = 0.5
    y = 0.6
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
        y += h* eiler(x, y)
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.title("grafic 1 Eiler method")
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

def method2(eiler_koshi, x, y):
    h = 0.1
    x = 0.7
    y = 2.1
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
       
        y += h/2 * (eiler_koshi(x, y) + eiler_koshi(x+h, eiler_koshi(x, y)))
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.title("grafik 2 Koshi method")
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

print(method1(eiler, 0.5, 1.5))
print(method2(eiler_koshi, 0.7, 1.7))