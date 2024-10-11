class BaseClass: pass # pragma: no cover
def compile_rules(): pass # pragma: no cover

a = (1, 2, 3) # pragma: no cover
kw = {'key': 'value'} # pragma: no cover
self = type('Derived', (BaseClass,), {'_compile_rules': compile_rules})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
