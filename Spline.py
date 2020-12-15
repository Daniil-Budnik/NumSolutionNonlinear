from NumSolutionNonlinear import *
from matplotlib.pyplot import*

#A = np.loadtxt("_A.txt")
#B = np.loadtxt("_B.txt")
#print(Sweep(A,B))

T = np.arange(0,1.1,0.01)
Tk = np.arange(0,1,0.003)
X = [ np.sin(x*10)*5 for x in T]

plot(T,X,'blue')
plot(Tk,Interpol(T,X, Tk),'green')
show()

