from twisted.internet import defer # pragma: no cover
def func(arg1, arg2): return arg1 + arg2 # pragma: no cover

defer = type('Mock', (object,), {'maybeDeferred': staticmethod(lambda f, *args, **kwargs: f(*args, **kwargs))})() # pragma: no cover
func = lambda x, y: x + y # pragma: no cover
a = (1, 2) # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
from l3.Runtime import _l_
aux = defer.maybeDeferred(func, *a, **kw)
_l_(7677)
exit(aux)
