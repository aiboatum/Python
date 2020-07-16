import collections
'''
    collections module implements specialized container datatypees providing alternatives
    to Python's general purpose built-in containers
    i.e.,dict,list,set,and tuple

    counter :dict subclass for counting hashable objects
    It's an unordered collection where elements are stored as dictionary
    keys and their counts are stored as dictionary values.
    Counts are allowed to be any integer value including zero or negative counts.


'''
#e.g.
cnt=collections.Counter()
for word in ['red','blue','red','blue','green']:
    cnt[word]+=1
#output is:Counter({'b': 9, 'a': 8, 'c': 5})
#print(cnt)

import re
words=re.findall(r'\w+',open('from.txt').read().lower())
#c=collections.Counter('abaaaaccbabcbabbcbabcb')
print(collections.Counter(words).most_common(3))

'''
    elements are counted from an iterable or initialized from another mapping(or counter)

'''
c=collections.Counter()#a new,empty counter
c=collections.Counter("ajlfjl")#a new from an iterable
c=collections.Counter({'red':4,"white":3})#a new from a mapping
c=collections.Counter(cats=4,dogs=8)#a new from keyword args
#print(c)
"""
    counter objects have a dictionary interface except that they return
    a zero count for missing items instead of raising a keyerror

"""
c=collections.Counter(['eggs','ham'])
c['fajfl']#count of a missing element is zero
#output is :0

'''

'''