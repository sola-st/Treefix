try: # pragma: no cover
    from itertools import izip as zip # pragma: no cover
except ImportError: # pragma: no cover
    pass # pragma: no cover

try: # pragma: no cover
    xrange # pragma: no cover
except NameError: # pragma: no cover
    xrange = range # pragma: no cover
 # pragma: no cover
dict = {i: i * 2 for i in range(10)} # pragma: no cover
 # pragma: no cover
class DictItemsWrapper(object): # pragma: no cover
    def __init__(self, d): # pragma: no cover
        self.dict = d # pragma: no cover
    def iteritems(self): # pragma: no cover
        return iter(self.dict.items()) # pragma: no cover
 # pragma: no cover
dict = DictItemsWrapper(dict) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems-in-python2
from l3.Runtime import _l_
dict = {i: i * 2 for i in xrange(10000000)}  
_l_(14213)  
# Slow and memory hungry.
for key, value in dict.items():
    _l_(14215)

    print(key,":",value)
    _l_(14214)

dict = {i: i * 2 for i in xrange(10000000)}  
_l_(14216)  
# More memory efficient.
for key, value in dict.iteritems():
    _l_(14218)

    print(key,":",value)
    _l_(14217)

