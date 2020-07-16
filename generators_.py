"""
    generator 可以创建一个iterator
    遍历时通过next()函数获得下一个元素
    通过修改next()方法即可修改推算下一个元素的算法
"""
def myrange_anotherone(a,b):#此def不是通过generator来创建迭代对象
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b#此处相当于t=(b,a+b),t是一个tuple,a=t[0],b=t[1],与c区别
        n+=1
    return "Done!"

"""
    generator使用yield 关键字
"""
def myrange(a,b):

    while a<b:
        yield a
        a+=1
"""
    生成器是构成迭代器的一个函数
"""
def squares(a,b):
    for value in range(a,b+1):
        yield value**2

def my_generator_1(n):
    for i in range(1,n+1):
        if i%2!=0:
            yield i
def my_generator_2(n):
    while n>=0:
        value=n
        n-=1
        yield value
def my_generator_3(n):
    
    def fib(x):
        if x==0:
            return 0
        if x==1:
            return 1
        pre1=0
        pre2=1
        while x>=2:
            x-=1
            pre=pre1+pre2
            pre2=pre1
            pre1=pre
        return pre
    
    for i in range(n+1):
        yield fib(i)

#返回一个fib数列
def my_generator_4(x):
        pre1=0
        pre2=1
        while x!=-1:
            x-=1
            yield pre1
            pre=pre1+pre2
            pre2=pre1
            pre1=pre
    
def my_generator_5(n):
    for i in range(n):
        yield i,i+1
#for value in my_generator_5(10):
 #   print(value)   
    
my_generator=(x for x in range(3))
"""
    简单创建generator的方法：
    类似于list中的 [x for x in range(3)]
    {x:x**2 for x in range(3)}
    而复杂的next()方法无法通过以上类似list生成式来实现的时候
    通过函数来实现
"""
#for value in my_generator:
   #print(" ",value)

#for value in squares(10):
 #   print(value)

"""
    generator和普通函数执行流程不同，函数顺序执行，遇到return语句返回
    而生成generator的函数，每次调用next()的时候执行，遇到yield语句返回
    再次执行时从上次返回到yield语句处继续执行
"""
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield(3)
    print("step 3")
    yield 5
o=odd()
print(next(o))
print(next(o))

for value in o:
    print(value)
