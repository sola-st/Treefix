from future import standard_library # pragma: no cover
standard_library.install_hooks() # pragma: no cover
from builtins import range # pragma: no cover

xrange = range # pragma: no cover

xrange = range # pragma: no cover
dict = {i: i * 2 for i in range(10000000)} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems-in-python2
from l3.Runtime import _l_
dict = {i: i * 2 for i in xrange(10000000)}  
_l_(1990)  
# Slow and memory hungry.
for key, value in dict.items():
    _l_(1992)

    print(key,":",value)
    _l_(1991)

dict = {i: i * 2 for i in xrange(10000000)}  
_l_(1993)  
# More memory efficient.
for key, value in dict.iteritems():
    _l_(1995)

    print(key,":",value)
    _l_(1994)

