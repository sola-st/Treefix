class Mock: pass # pragma: no cover
from typing import Any, Dict # pragma: no cover

a = [] # pragma: no cover
kw = {} # pragma: no cover
self = type('MockClass', (Mock,), {'_compile_rules': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
