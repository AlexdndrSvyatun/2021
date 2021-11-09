from numpy import *
from math import *
import copy
import matplotlib.pyplot as plt

masx = [0.190,0.195,0.200,0.205,0.210,0.215,0.220]
masy = [5.3263,5.1930,5.0664,4.9461,4.8317,4.7226,4.6185]

x1 = 0.193
x2 = 0.216

h = masx[1] - masx[0]

q1 = (x1 - masx[0]) / h
q2 = (x2 - masx[-1]) / h

def y(masy, k):

    arr = []

    for i in range(len(masy)):
        arr.append(masy[i] - masy[i-1])

    arr.pop(0)

    if k == 1:
        return arr

    else:
        k -= 1
        return y(arr, k)

n1 = masy[0] + q1 * y(masy, 1)[0]
n2 = masy[-1] + q2 * y(masy, 1)[-2]

dod1 = []
dod2 = []

d1 = copy.copy(q1)
d2 = copy.copy(q2)

for i in range (len(masx)):
    d1 = d1 * (q1 - i)
    d2 = d2 * (q2 + i)
    dod1.append(d1)
    dod2.append(d2)

for i, j, k in zip(range (len(masx)-2), range(2, len(masx)), range(len(masx)-2, 0)):
    n1 = n1 + dod1[i] / factorial(j) * y(masy, j)[0]
    n2 = n2 + dod2[i] / factorial(j) * y(masy, j)[k]

print(n1)
print(n2)

plt.plot(masx, masy, '.-', color = '#ADFF2F')
plt.plot(x1, n1, 'o', color = '#1E90FF')
plt.plot( x2, n2, 'o', color = '#000000')
plt.xlabel('x')
plt.ylabel('y')
plt.title('function grafic')
plt.legend(['y = N(x)', 'f(x1)', 'f(x2)'])
plt.grid()
plt.show()