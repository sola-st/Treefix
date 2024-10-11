class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._stats = {'status': 'ok', 'code': 0} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
aux = self._stats
_l_(8640)
exit(aux)
