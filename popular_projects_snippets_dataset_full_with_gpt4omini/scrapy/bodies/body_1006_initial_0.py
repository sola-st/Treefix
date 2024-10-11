from collections.abc import Iterable, AsyncIterable # pragma: no cover

o = [1, 2, 3]  # An example of a concrete iterable # pragma: no cover
Iterable = Iterable  # Reference to the Iterable class # pragma: no cover
AsyncIterable = AsyncIterable  # Reference to the AsyncIterable class # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = isinstance(o, (Iterable, AsyncIterable))
_l_(9752)
exit(aux)
