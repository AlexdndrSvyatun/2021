import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
import sympy as sp
from matplotlib import style

x = [0.7, 1.1, 1.4, 1.9, 2.6]
y = [2.75, 3.87, 1.25, 4.26, 2.43]



xs = linspace(x[0], x[-1], 100)

x_i = sp.symbols('x_i')

h = []
m = []
k = []
alpha = [0, 0]
beta = [0, 0]
a = y
b = [0]
c = [0]
d = [0]

ys = []

def spline_fun(xk):

    for i in range(len(x)):
        h_i = x[i] - x[i-1]
        h.append(h_i)
   

    for i in range(len(h)):
        m_i = 2 * (h[i-1] + h[i])
        m.append(m_i)
    

    for i in range(len(h)):
        k_i = 3 * ( ((y[i] - y[i-1]) / h[i]) - ((y[i-1] - y[i-2]) / h[i-1]) )
        k.append(k_i)

    for i in range (2, len(h)):
        alpha_i = (k[i] - h[i-1]*alpha[i-1]) / (m[i] - h[i-1]*beta[i-1])
        alpha.append(alpha_i)
        beta_i = h[i] / (m[i] - h[i-1]*beta[i-1])
        beta.append(beta_i)

    for i in range (1, len(alpha)):
        c_i = alpha[-i] - beta[-i]*c[-i]
        c.insert(0, c_i)

    i = len(c) - 1
    while i >= 0:
        d_i = (c[i]-c[i-1]) / (3 * h[i])
        d.insert(0, d_i)
        i-=1

    i = len(c) - 1
    while i >= 0:
        b_i = ((y[i] - y[i-1]) / h[i]) - (((c[i] + 2*c[i-1]) * h[i] )/ 3)
        b.insert(0, b_i)
        i -= 1
    #print(b)

    print('\nspline:\n')
    for i in range(len(c)-1):
        s_i = a[i] + b[i+1]*(x_i - x[i]) + c[i]*((x_i-x[i])**2) + d[i+1]*((x_i-x[i])**3)
        print(s_i)

    def spline(i, x_j):
        s_ij = a[i] + b[i+1]*(x_j - x[i]) + c[i]*((x_j-x[i])**2) + d[i+1]*((x_j-x[i])**3)
        return s_ij

    print('\n\nspline:\n')
    for i in range(len(x)-1):
        print(spline(i, x[i]))
    print('\n')

    i = len(xk)-1 
    j = len(x)-1

    while i >= 0:

        while (xk[i] >= x[j]):
            yi = spline(j, xk[i])
            ys.insert(0, yi)
            if i == 0:
                break
            i -= 1

        if j == 0:
           break
        j -= 1 

    return ys

xsl = xs.tolist()
spl = spline_fun(xsl)

spl1 = UnivariateSpline(x, y)

style.use('seaborn-whitegrid')

plt.plot( xs, spl, color = '#008B8B')
plt.plot(xs, spl1(xs), '--', color = '#000000')
plt.plot(x, y, '.', color = '#FF0000' )

plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline ')
plt.legend(['spline color', 'UnivariateSpline', 'data'])

plt.show()

