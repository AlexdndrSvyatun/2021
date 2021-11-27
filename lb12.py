from math import *
from numpy import *
from matplotlib import style
import matplotlib.pyplot as plt

xi = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5]

def f(x):
    y = sin(cos(x))
    return y

yi = []

for i in range(len(xi)):
    yi.append(f(xi[i]))

def square_fun(x):

    print('\n')

    sum = 0
    for i in range(len(xi)):
        sum = sum + xi[i]
    xa = sum/len(xi)
    print('x average =', xa)

    sum = 0
    for i in range(len(xi)):
        sum = sum + xi[i]**2
    x2a = sum/len(xi)
    print('x**2 average =', x2a)

    sum = 0
    for i in range(len(yi)):
        sum = sum + yi[i]
    ya = sum/len(yi)
    print('y average =', ya)

    sum = 0
    for i in range(len(xi)):
        sum = sum + xi[i]*yi[i]
    xya = sum/len(xi)
    print('x*y average =', xya)

    print('\n')

    a1 = (xya - xa*ya) / (x2a - xa**2)
    print('a1 =', a1)

    a0 = ya - a1*xa
    print('a0 =', a0)

    print('\n')

    if (a1 < 0):
        print(f'f(x) = {a0} {a1} * x')
    else:
        print(f'f(x) = {a0} + {a1} * x')

    print('\n')

    return a0 + a1*x

xs = linspace(min(xi), max(xi), 100)
ys = square_fun(xs)

style.use('seaborn-whitegrid')
plt.plot(xi, yi, 'g.')
plt.plot(xs, ys, color = '#000000')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least squares function approximation')
plt.legend(['points', 'Approximate schedule'])
plt.show()