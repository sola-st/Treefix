from typing import Any, Dict # pragma: no cover

class MockBaseClass: # pragma: no cover
    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None: # pragma: no cover
        print('super().__init__ executed') # pragma: no cover
 # pragma: no cover
def mock_compile_rules(self) -> None: # pragma: no cover
    print('_compile_rules executed') # pragma: no cover
 # pragma: no cover
a: Any = () # pragma: no cover
kw: Dict[str, Any] = {} # pragma: no cover
 # pragma: no cover
class MockDerivedClass(MockBaseClass): # pragma: no cover
    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None: # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
        self._compile_rules() # pragma: no cover
 # pragma: no cover
    _compile_rules = mock_compile_rules # pragma: no cover
 # pragma: no cover
self = MockDerivedClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(19807)
self._compile_rules()
_l_(19808)
