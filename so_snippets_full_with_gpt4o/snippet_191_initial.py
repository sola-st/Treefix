# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
from l3.Runtime import _l_
try:
    import timeit
    _l_(12153)

except ImportError:
    pass
print(timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9,10]', number=1000000)) #created list
_l_(12154) #created list
print(timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9,10)', number=1000000)) # created tuple 
_l_(12155) # created tuple 

0.136621
_l_(12156)
0.013722200000000018
_l_(12157)

