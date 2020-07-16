import random
def permutation(x):
    y=[0]*9
    y[0]=x[1]
    y[1]=x[6]
    y[2]=x[7]
    y[3]=x[4]
    y[4]=x[8]
    y[5]=x[2]
    y[6]=x[5]
    y[7]=x[3]
    y[8]=x[0]
    return y
x=[]
for i in range(9):
    x.append(random.randint(0,1))
print(x)
print(permutation(x))