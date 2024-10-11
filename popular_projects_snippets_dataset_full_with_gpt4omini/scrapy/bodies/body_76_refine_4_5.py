from unittest.mock import Mock # pragma: no cover

a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
self = type('MockSelf', (object,), {'_compile_rules': Mock()})() # pragma: no cover

class BaseClass: pass # pragma: no cover

class MyClass(BaseClass): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        pass
 # pragma: no cover
self = MyClass(1, 2, 3, key1='value1', key2='value2') # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
