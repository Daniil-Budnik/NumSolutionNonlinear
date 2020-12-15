from NumSolutionNonlinear import *

# -------------------------------------------

#A = [[1,2,3],
#     [5,7,8],
#     [9,4,3]]
#
#Q,R = QR(A)
#
#for i in Q: print(i) 
#print()
#for i in R: print(i)
#print()
#print(np.dot(Q,R))

# -------------------------------------------

def f1(x): return 2 * (x**2)
def f2(x): return 6 * x
def f3(x): return 4

def F(x): return f1(x) + f2(x) + f3(x)

X = np.arange(0,3,0.01)
Z = [ [f1(x), f2(x), f3(x)] for x in X ]
print(QR_MNK(Z))