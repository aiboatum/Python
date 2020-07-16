'''
    list may constructed in several ways:
    using a list conprehension :[x for x in iterable ]
    using the type constructor :list()or list(iterable)
    take much count for the following:
    list(iterable)if iterable is already a list,a copy is made and returned
    similar to iterable[:]
'''
squares=[]
for x in range(10):
    squares.append(x**2)


squares=list(map(lambda x:x**2,range(10)))


l=[(x,y) for x in range(1,4) for y in [3,1,4] if x!=y]

#equivalent to the following
combs=[]
for x in range(1,4):
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))


vec=[-4,-2,0,2,4]
#create a new list with the values doubled
print([x*2 for x in vec])
#filter the list to exclude negative numbers
print([x for x in vec if x>=0])
#apply a function to all the elements
print([abs(x) for x in vec])
#call a method on each element
freshfruit=['   banana','loganberry','passion fruit']
print([weapon.strip() for weapon in freshfruit])
"""
strip()方法可以去除首尾指定字符
"""
#create a list of 2-tuples like (number,square)
print([(x,x**2)for x in range(6)])

#flatten a list using a listcomp with two 'for'
vec=[list(range(1,4)),list(range(4,7)),list(range(7,10))]
print("vec :")
print(vec)
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi,i))for i in range(1,6)])

print([i**2 for i in range(1,11)])

print([i**3 for i in range(1,21)])

print([e for e in range(20) if e%2==0])

print([e for e in range(20) if e%2!=0])

print([e**2 for e in range(20)if e%2==0])
# list with the squares of the even numbers from 0 to 20, and sum the list
print((sum([e**2 for e in range(20)if e%2==0])))

print([e**2 for e in range(20)if e%2==0 and e%3!=0])

