"""
    coroutine接受外部.send()方法传过来的value
    
    通过.next()方法,start这个coroutine
  
    每一次调用send()方法,参数会通过yield传进来
    .next()方法到下一个元素
    .close()方法关闭这个coroutine
"""
def coroutine():
    print("My coroutine")
    while True:
        val=yield
        print("Got",val)



def fib(n):
    a,b,max=0,1,0
    while max<=n:
        max+=1
        yield a
        a,b=b,a+b
#for i in fib(10):
 #   print(i)

def gerp(pattern):
    print("searching for ",pattern)
    while True:
        line=yield
        if pattern in line:
            print(line)
# searhc=gerp("coroutine")
# next(searhc)
# #output:searching for coroutine
# searhc.send("i love you ")
# searhc.send("don't you love me?")
# searhc.send("i love coroutine instead!")
# #output:i love coroutine instead!
# searhc.close()
# #close the pipeline data      

def square():
    while True:
        value=yield
        value_=int(value)
        print(value_**2)

def mimimize():
    value=yield
    min=int(value)
    while True:
        value=yield
        value=int(value)
        if value<min:
            min=value
            print("current min number is:",min)
"""    
mi=mimimize()
next(mi)
mi.send(10)
mi.send(11)
mi.send(1)
mi.send(0)
mi.send(-1)
mi.close()
"""

