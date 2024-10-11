from typing import Any # pragma: no cover

a: Any = () # pragma: no cover
kw: dict = {} # pragma: no cover
class MockSuperClass: # pragma: no cover
    def __init__(self, *args: Any, **kwargs: dict) -> None: # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def mock_compile_rules(self) -> None: # pragma: no cover
    print('_compile_rules executed') # pragma: no cover
 # pragma: no cover
MockClass = type('MockClass', (MockSuperClass,), {'_compile_rules': mock_compile_rules}) # pragma: no cover
self = MockClass() # pragma: no cover
self.__init__(*a, **kw) # pragma: no cover
self._compile_rules() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
