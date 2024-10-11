class ABaseClass:# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
def compile_rules():# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover

class MockSuperClass(ABaseClass):# pragma: no cover
    def __init__(self, *a, **kw):# pragma: no cover
        super().__init__(*a, **kw)# pragma: no cover
 # pragma: no cover
type('Mock', (MockSuperClass,), {'_compile_rules': compile_rules}) # pragma: no cover
self = type('MockInstance', (MockSuperClass,), {'_compile_rules': compile_rules})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
