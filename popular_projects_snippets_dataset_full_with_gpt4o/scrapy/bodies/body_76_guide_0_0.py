from typing import Any # pragma: no cover

a: Any = () # pragma: no cover
kw: dict = {} # pragma: no cover
class MockSuperClass: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (MockSuperClass,), {'_compile_rules': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
