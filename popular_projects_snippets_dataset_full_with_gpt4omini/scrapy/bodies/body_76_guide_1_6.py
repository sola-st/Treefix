class MockBase: pass # pragma: no cover
class DerivedClass(MockBase): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        super().__init__(*a, **kw) # pragma: no cover
        self._compile_rules() # pragma: no cover
    def _compile_rules(self): # pragma: no cover
        print('Compiling rules...') # pragma: no cover

a = (1, 2) # pragma: no cover
kw = {'arg1': 'value1'} # pragma: no cover
instance = DerivedClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
