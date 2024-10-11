from typing import Callable # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._read_unicode = lambda n: 'unicode string' * (n // 14) # pragma: no cover
self._read_string = lambda n: 'string' * (n // 6) # pragma: no cover
self._is_unicode = True # pragma: no cover
n = 28 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
self.read = self._read_unicode if self._is_unicode else self._read_string
_l_(7358)
aux = self.read(n).lstrip()
_l_(7359)
exit(aux)
