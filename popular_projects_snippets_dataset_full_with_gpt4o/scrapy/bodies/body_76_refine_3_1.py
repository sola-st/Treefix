a = () # pragma: no cover
kw = {} # pragma: no cover
self = type('Mock', (object,), {'_compile_rules': lambda self: None})() # pragma: no cover

class Base:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover
self = type('Mock', (Base,), {'_compile_rules': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
