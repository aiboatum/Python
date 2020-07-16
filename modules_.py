import math
print(math.cos(0.0))

print(math.radians(275))

print(math.gcd(15,21),math.gcd(152,200),math.gcd(1988,9765))

#自定义实现gcd方法
def gcd_1(a,b):
    if b%a==0:
        return a 
    return gcd_1(b%a,a)
print(gcd_1(15,21),gcd_1(152,200),gcd_1(1988,9765))


"""
#implement the "add2"function that receives two numbers as arguments
def add2():
    a=int(input())
    b=int(input())
    print(a+b)
add2()

def add3(a,b,c):
    return a+b+c
n1=int(input())
n2=int(input())
n3=int(input())
print(add3(n1,n2,n3))
"""

def ave(l):
    return sum(l)/len(l)
print(ave([1,2,3,4]))

#recursive part
def factorial(x):
    if x==0:
        return 1
    else :
        return x*factorial(x-1)

def fib(x):
    if x==0:
        return 0
    if x==1 :
        return 1
    return fib(x-1)+fib(x-2)
print(fib(7))