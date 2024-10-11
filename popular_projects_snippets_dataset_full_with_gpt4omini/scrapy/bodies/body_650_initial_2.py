from twisted.internet import defer # pragma: no cover

def func(): return 'Hello, World!' # pragma: no cover
a = [1, 2, 3] # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
from l3.Runtime import _l_
aux = defer.maybeDeferred(func, *a, **kw)
_l_(7677)
exit(aux)
