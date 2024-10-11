from typing import Any # pragma: no cover
class Mock: pass # pragma: no cover

self = type('Mock', (object,), {'_compile_rules': lambda self: None})() # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

class Base: pass # pragma: no cover
class Mock(Base): pass # pragma: no cover

self = type('Mock', (Base,), {'_compile_rules': lambda self: None})() # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
