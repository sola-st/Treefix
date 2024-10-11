from typing import Any, Tuple # pragma: no cover

a: Tuple[Any] = () # pragma: no cover
self = type('Mock', (object,), {'_compile_rules': lambda self: 'Compiled'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
