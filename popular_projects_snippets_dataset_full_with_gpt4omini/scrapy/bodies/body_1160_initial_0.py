class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._meta = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
from l3.Runtime import _l_
if self._meta is None:
    _l_(4738)

    self._meta = {}
    _l_(4737)
aux = self._meta
_l_(4739)
exit(aux)
