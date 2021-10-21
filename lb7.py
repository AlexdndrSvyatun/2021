from numpy import*
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
x = array([-2.5,-0.5,1,2],dtype = float)
y = array([3.6,3.03,5.1,10.1],dtype = float)
def L(x,y,k):
	summa = 0
	for g in range (len (y)):
		p1 = 1
		p2 = 1
		for i in range (len (x)):
			if i == g :
				p1 *= 1
				p2 *= 1
		else :
				p1 *= (k-x[i])
				p2 *= (x[g]-x[i])
		summa += y[g]* p1/p2
	return summa
xnew = linspace (min(x), max(x))
ynew = [L(x,y,i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.title('grafik')
plt.grid(axis="both")
plt.show()

f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynom')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()