from unittest.mock import MagicMock # pragma: no cover

a = (1, 2, 3) # pragma: no cover
kw = {'param1': 'value1', 'param2': 'value2'} # pragma: no cover
self = type('MockSelf', (object,), {'_compile_rules': MagicMock()})() # pragma: no cover

from typing import Any, Tuple, Dict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
from l3.Runtime import _l_
super().__init__(*a, **kw)
_l_(8832)
self._compile_rules()
_l_(8833)
