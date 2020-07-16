#-*- encoding:utf-8 -*-
import re
fo=open("C:/Python_test/from.txt")
ot=open("C:/Python_test/ot.txt")
t_reseult=[]
while True:
    line=fo.readline()
    if not line:
        fo.close()
        break
    else:
        line=re.sub(r'[^A-Za-z','',line)
        lise_line=line.split()
        for i in lise_line:
            t_reseult.append(i)
def order_by_str(x):
    temp=[]
    res=[]
    for i in x:
        temp.append((i.lower(),i))
    temp.sort()
    for l in temp:
        res.append(l[i])
    return res
result=order_by_str(t_reseult)
for i in result:
    ot.write(i+'\n')
ot.close()     