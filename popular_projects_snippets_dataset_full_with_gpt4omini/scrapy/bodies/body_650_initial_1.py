from twisted.internet import defer # pragma: no cover

def func(): return 'function executed' # pragma: no cover
a = [1, 2, 3] # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
defer.maybeDeferred = type('Mock', (object,), {'__call__': lambda self, func, *args, **kwargs: defer.succeed(func(*args, **kwargs))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
from l3.Runtime import _l_
aux = defer.maybeDeferred(func, *a, **kw)
_l_(7677)
exit(aux)
