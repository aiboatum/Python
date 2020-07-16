"""
    dict()->new empty dictionary
    dict(mapping)->new dictionary initialized from a mapping object's
    (key,value)pairs
    dict(iterable)->new dictionary initialized as if via:
    d={}
    for k,v in iterable:
        d[k]=v
    dict(**kwargs)->new dictionary initialized with the name=value pairs
    in the keyword argument list.For example:dict(one=1,two=2)

"""
ages={"peter":10,
"isabel":11,
"anna":9,
"thomas":10,
"bob":10
}
for name,age in ages.items():
    print(name,age)

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}


def ave_dic(dic):
    sum=0
    for age in dic.values():
        sum+=age
    return sum/len(dic)

def oldest_person(dic):
    oldest=0
    for key in dic.keys():
        if dic[key]>oldest:
            oldest=dic[key]
            key_=key
    return key_

def new_ages(dic,n):
    return_dic={}
    for key,value in dic.items():
        return_dic[key]=value+n
    return return_dic
#print(new_ages(ages,10))
students = {
"Peter": {"age": 10, "address": "Lisbon"},
"Isabel": {"age": 11, "address": "Sesimbra"},
"Anna": {"age": 9, "address": "Lisbon"},
}
#print(len(students))
def ave_student(stu):
    sum=0
    for dic in stu.values():
        sum+=dic["age"]
    return sum/len(stu)

#print(ave_student(students))
def find_students(stu,str_):
    reutrn_name=[]
    for name in stu.keys():
        if stu[name]["address"]==str_:
            reutrn_name.append(name)
    return reutrn_name
print(find_students(students,"Lisbon"))