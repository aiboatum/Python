"""
iterator classes
iterator can be implemented as classes,we just need to implement the
__next__ and __iter__ methods.
"""

class  MyRange(object):
    
    def __init__(self,a,b):
        self.start=a
        self.stop=b
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<self.stop:
            value=self.start
            self.start+=1
            return value**2
        else:
            raise StopIteration

class MyRange_1(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.a<self.b :
            if self.a%2==0:
                value=self.a
                self.a+=2
                return value
            else:
                self.a+=1
                pass
        else:
            raise StopIteration
        
class MyRange_2(object):
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.a<=self.b:
            value=self.b
            self.b-=1
            return value
        else:
            raise StopIteration

class MyRange_3(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __iter__(self):
        return self
    def fib(self,n):
            if n==0:
                return 0
            if n==1:
                return 1
            pre1=0
            pre2=1
            while n>=2:
                n-=1
                pre=pre1+pre2
                pre1=pre2
                pre2=pre
            return pre
    def __next__(self):
        if self.a<=self.b:
            value=self.fib(self.a)
            self.a+=1
            return value
        else:
            raise StopIteration

class fab(object):
    def __init__(self,n):
        self.pre1=0
        self.pre2=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>=0:
            self.n-=1
            value=self.pre1
            pre=self.pre1+self.pre2
            self.pre2=self.pre1
            self.pre1=pre
            return value
        else :
            raise StopIteration
class MyRange_4(object):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a<self.b:
            value=self.a
            self.a+=1
            return value,value+1
        else:
            raise StopIteration

for value in fab(10):
    print(value)           
# myrange=MyRange_4(0,10)
# for value in myrange:
#     print(value)
