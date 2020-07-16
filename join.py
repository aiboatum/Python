"""
    python s.join()method
    s.join(iterable),namely str,list,tuple,dict or other interable
    
"""
#list:
def list_():
    #output :0-1-2-3-4-5-6-7-8-9
    print("{0}".format('-'.join([str(x) for x in range(10)])))
#str
def str_():
    #output :o*l*l*e*h
    s="hello"
    print("{0}".format('*'.join(s[::-1])))
#tuple
def tuple_():
    #output :0+1+2+3
    print("{0}".format('+'.join((str(x) for x in range(4)))))
#dict
def dict_():
    #output :0-1-2
    print("{0}".format("-".join({str(x):x**2 for x in range(3)})))
