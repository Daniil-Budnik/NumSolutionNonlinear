from NumSolutionNonlinear import *
from random import gauss

Xn = np.arange(-3,3,0.0001)
Yn = [ (10 + 8*x + 5 * (x**2) + 15*(x**3)) + gauss(0,0.05) for x in Xn ]

np.savetxt('_X.txt',Xn)
np.savetxt('_Y.txt',Yn)

Xn = np.loadtxt('_X.txt')
Yn = np.loadtxt('_Y.txt')

An, Bn = MNK(Xn, Yn, 4)

for i in range(len(An)): print(An[i]) 
print()
print(Bn)
print()
print(Gauss(An,Bn))

#An = np.loadtxt("_A1.txt")
#Bn = np.loadtxt("_B1.txt")

#print(Gauss(An,Bn))