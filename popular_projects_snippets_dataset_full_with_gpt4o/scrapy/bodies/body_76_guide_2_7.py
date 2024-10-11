class MockBase: # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        pass # pragma: no cover

a = () # pragma: no cover
kw = {} # pragma: no cover
class Mock(MockBase): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        super().__init__(*a, **kw)  # This will be executed # pragma: no cover
 # pragma: no cover
    def _compile_rules(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
mock_instance = Mock(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
