'''
    测试map method 
    map(func,iterables)-->map object
    make an iterator that computes the func using arguments from
    each of the iterables.Stops when the shortest iterables is exhausted.
    a iterable object is returned by map method 
'''
l=map(lambda x,y:x+y,[i for i in range(10)])
print(l)
#output is :<map object at 0x0000018FD7AFA550>
