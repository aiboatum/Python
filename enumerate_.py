"""
    enumerate(iterable,start=0)
    return an enumerate object.
    iterable must be an sequence ,an iterator,
    or some other which supports iteration.
    The __next__()method of the iterator returned by enumerate()
    returns a tuple contining a count
    (from start which defaults to 0) 
"""
sersons=['spring','summer','fall','winter']
print(dict(enumerate(sersons)))
print(list(enumerate(sersons,start=1)))
#equivalent to:
def enumerate(sequence,start=0):
    n=start
    for elm in sequence:
        yield n,elm
        n+=1