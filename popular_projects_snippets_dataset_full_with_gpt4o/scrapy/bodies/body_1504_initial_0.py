from typing import List # pragma: no cover

result = [1, 2, 3] # pragma: no cover
response = 'A response mock' # pragma: no cover
self = type('Mock', (object,), {'_set_referer': lambda self, r, response: response})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
aux = (self._set_referer(r, response) for r in result or ())
_l_(16477)
exit(aux)
