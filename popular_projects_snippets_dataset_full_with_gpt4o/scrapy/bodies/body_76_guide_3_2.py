class MockSuperClass: # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        pass # pragma: no cover

a = () # pragma: no cover
kw = {} # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        super(Mock, self).__init__(*a, **kw) # pragma: no cover
        print('super executed') # pragma: no cover
 # pragma: no cover
self = type('Mock', (MockSuperClass,), {})() # pragma: no cover
self.__init__(*a, **kw) # pragma: no cover
self._compile_rules = lambda: print('_compile_rules executed') # pragma: no cover
self._compile_rules() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
