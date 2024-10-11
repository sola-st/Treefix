a = [] # pragma: no cover
kw = {} # pragma: no cover
class MockBaseClass:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
self = MockBaseClass() # pragma: no cover
def _compile_rules(self):# pragma: no cover
    pass # pragma: no cover
self._compile_rules = _compile_rules.__get__(self) # pragma: no cover

a = () # pragma: no cover
kw = {} # pragma: no cover
class BaseClass:# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        super().__init__(*args, **kwargs)# pragma: no cover
    def _compile_rules(self):# pragma: no cover
        print('Compiling rules...') # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
