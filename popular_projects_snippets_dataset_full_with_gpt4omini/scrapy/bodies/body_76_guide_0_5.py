from typing import Any, Dict # pragma: no cover
class Base: pass # pragma: no cover

a = (1, 2, 3) # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
class Derived(Base): # pragma: no cover
    def __init__(self, *a: Any, **kw: Dict[str, Any]): # pragma: no cover
        super().__init__(*a, **kw) # pragma: no cover
        self._compile_rules() # pragma: no cover
    def _compile_rules(self): # pragma: no cover
        print('Rules compiled') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
