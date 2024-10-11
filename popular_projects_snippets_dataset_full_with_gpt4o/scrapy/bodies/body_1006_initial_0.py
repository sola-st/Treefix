from collections.abc import Iterable, AsyncIterable # pragma: no cover

o = [] # pragma: no cover
Iterable = Iterable # pragma: no cover
AsyncIterable = AsyncIterable # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = isinstance(o, (Iterable, AsyncIterable))
_l_(20966)
exit(aux)
