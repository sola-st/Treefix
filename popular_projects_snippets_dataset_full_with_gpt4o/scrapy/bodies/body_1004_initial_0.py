import warnings # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

self = type('MockSelf', (object,), {'slot': True})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
warnings.warn("ExecutionEngine.has_capacity is deprecated", ScrapyDeprecationWarning, stacklevel=2)
_l_(20222)
aux = not bool(self.slot)
_l_(20223)
exit(aux)
