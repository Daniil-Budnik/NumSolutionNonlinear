from NumSolutionNonlinear import *
import matplotlib.pyplot as plt
from random import uniform

# -------------------------------------------------------------

def F(x): return 3*(x**3) + 5*(x**2) - 5*x + 10

# -------------------------------------------------------------
plt.subplot(3,1,1)

X1 = np.arange(-2,2,0.05)
Y1 = [ F(x) for x in X1 ]

plt.plot(X1,Y1,color="blue")

# -------------------------------------------------------------

plt.subplot(3,1,2)

X2 = np.arange(-2,3,1)
Y2 = [ F(x) for x in X2 ]
Y3 = [Lagranz(X2,Y2,x) for x in X1]

plt.plot(X2,Y2,color="green")
plt.plot(X1,Y3,"--o",color="red")

# -------------------------------------------------------------

plt.subplot(3,1,3)

X4, xn = [], -2
X4.append(xn)
while(xn < 2): 
    xn += uniform(0.5,1)
    X4.append(xn)
Y4 = [ F(x) for x in X4 ]

X5 = np.linspace(-2,2,100)
Y5 = [Lagranz(X4,Y4,x) for x in X5]

plt.plot(X4,Y4,color="green")
plt.plot(X5,Y5,"--o",color="red")

# -------------------------------------------------------------

plt.show()
