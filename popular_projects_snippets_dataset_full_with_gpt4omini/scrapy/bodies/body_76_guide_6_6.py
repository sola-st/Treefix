class Base: pass # pragma: no cover
class MockClass(Base): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
        self._compile_rules = lambda: 'Compilation complete!' # pragma: no cover

a = ('arg1', 'arg2') # pragma: no cover
kw = {'option1': True, 'option2': 42} # pragma: no cover
instance = MockClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
