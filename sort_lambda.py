#lambda表达式
'''
    list.sort(key=None,reverse=False):对list排序，reverse缺省为false，即增
    sorted(iterable,key=None,reverse=False)：返回一个排好序的副本，原iterable不变

e.g.            
lambda x:x**2
<=>
def f(x):
    return x**2

e.g.
def foo(x):
    return lambda y:x+y
<=>
def foo(x):
    def lambda_(y):return x+y
    return lambda_(y)
<=>
lambda x :lambda y:x+y
'''

#多级排序
#先按第三个排序即lambda x:int(x[2])
#再按第二个排序即lambda x:int(x[1])
print(sorted([('2', '3', '10'), ('1', '2', '3'), ('5', '6', '7'), \
('2', '5', '10'), ('1', '4', '10')],key=lambda x:(int(x[2]),int(x[1]))\
,reverse=False))
#[('1', '2', '3'), ('5', '6', '7'),\
#  ('2', '3', '10'), ('2', '4', '10'), ('2', '5', '10')]

#先按数字排序，再按偶数排序，
#再按大写字母排序，再按照小写排序
lis=sorted("9a13C85c7B24A6b",key=lambda x:(x.isdigit(),x.isdigit() \
and int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
print("".join(lis))



list1 = [('david', 90), ('mary',90), ('sara',80),('lily',95)]
#[('david', 90), ('lily', 95), ('mary', 90), ('sara', 80)]

print(sorted(list1,key=lambda list1:list1[0][1]))
#[('david', 90), ('mary', 90), ('sara', 80), ('lily', 95)]

