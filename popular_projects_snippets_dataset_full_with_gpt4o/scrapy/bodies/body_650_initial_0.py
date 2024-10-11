from twisted.internet import defer # pragma: no cover

defer = type('Mock', (object,), {'maybeDeferred': staticmethod(lambda f, *args, **kwargs: f(*args, **kwargs))})() # pragma: no cover
func = lambda *args, **kwargs: 'Function Executed' # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
from l3.Runtime import _l_
aux = defer.maybeDeferred(func, *a, **kw)
_l_(18560)
exit(aux)
