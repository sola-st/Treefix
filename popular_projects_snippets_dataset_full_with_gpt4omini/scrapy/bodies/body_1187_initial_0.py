from typing import Optional # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._encoding = None # pragma: no cover
self._bom_encoding = lambda: None # pragma: no cover
self._headers_encoding = lambda: None # pragma: no cover
self._body_declared_encoding = lambda: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
aux = (
    self._encoding
    or self._bom_encoding()
    or self._headers_encoding()
    or self._body_declared_encoding()
)
_l_(9181)
exit(aux)
