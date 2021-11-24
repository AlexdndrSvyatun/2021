from math import *
from numpy import *
import sympy as sp
from matplotlib import style

x = sp.symbols('x')

f = sp.sin(sp.cos(x))
n = 3

def taylor(x):

    d1 = sp.diff(f, x)
    d = d1
    y = f

    i = 1
    while i <= n:
        y = y + d*((x-0)**i)/factorial(i)
        d = sp.diff(d, x)
        i += 1
    
    print("\ny = ", y , "\n")
    return y

style.use('seaborn-whitegrid')

taylor_x = taylor(x)

p1 = sp.plot(f, (x, -2, 2),
title = "Polynom",
ylabel = "y", label = "f(x)", line_color = "#00e1ff",
show = False, legend = True)

p2 = sp.plot(taylor_x, (x, -2, 2), label = "ff(x)",
line_color = "#000000", show = False)



p1.append(p2[0])
p1.show()