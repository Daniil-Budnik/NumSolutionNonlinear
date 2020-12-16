from NumSolutionNonlinear import *
from matplotlib.pyplot import*


#A = np.loadtxt("_A.txt")
#B = np.loadtxt("_B.txt")
#print(Sweep(A,B))

#T = np.arange(0,1.01,0.01)
#Tk = np.arange(0.1,1,0.001)
#X = [ np.sin(x*10)*5 for x in T]

T = np.loadtxt("T.txt")
X = np.loadtxt("X.txt")
Tk = np.arange(-2.9,2.9,0.001)


scatter(T,X)
plot(Tk,Interpol(T,X, Tk),'green')

show()

