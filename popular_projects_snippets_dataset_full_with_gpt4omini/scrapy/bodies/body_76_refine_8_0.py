from typing import Any, Dict, Tuple # pragma: no cover

a: Tuple[Any] = () # pragma: no cover
kw: Dict[str, Any] = {} # pragma: no cover

class Base: pass # pragma: no cover
class Mock(Base):# pragma: no cover
    def _compile_rules(self): pass # pragma: no cover

a = () # pragma: no cover
kw = {} # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
