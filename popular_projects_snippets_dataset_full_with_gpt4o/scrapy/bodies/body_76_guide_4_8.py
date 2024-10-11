class BaseClass: # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        print('BaseClass __init__ executed') # pragma: no cover

a = () # pragma: no cover
kw = {} # pragma: no cover
class SubClass(BaseClass): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        super().__init__(*a, **kw)  # uncovered path # pragma: no cover
    def _compile_rules(self): # pragma: no cover
        print('_compile_rules executed')  # uncovered path # pragma: no cover
 # pragma: no cover
instance = SubClass(*a, **kw) # pragma: no cover
instance._compile_rules() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
