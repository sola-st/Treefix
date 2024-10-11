from builtins import range as xrange # pragma: no cover

class DictWithIteritems(dict): # pragma: no cover
    def iteritems(self): # pragma: no cover
        return iter(self.items()) # pragma: no cover
dict = DictWithIteritems() # pragma: no cover

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

