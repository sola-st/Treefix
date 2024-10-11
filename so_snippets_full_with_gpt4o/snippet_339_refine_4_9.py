xrange = range # pragma: no cover

from past.builtins import xrange # pragma: no cover

if not hasattr(collections, 'MutableMapping'): collections.MutableMapping = collections.abc.MutableMapping # pragma: no cover
class MockDict(collections.MutableMapping): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        self.store = dict(*args, **kwargs) # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return self.store[key] # pragma: no cover
    def __setitem__(self, key, value): # pragma: no cover
        self.store[key] = value # pragma: no cover
    def __delitem__(self, key): # pragma: no cover
        del self.store[key] # pragma: no cover
    def __iter__(self): # pragma: no cover
        return iter(self.store) # pragma: no cover
    def __len__(self): # pragma: no cover
        return len(self.store) # pragma: no cover
    def iteritems(self): # pragma: no cover
        return self.store.items() # pragma: no cover
dict = MockDict({i: i * 2 for i in xrange(10000000)}) # pragma: no cover

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

