class Mock:# pragma: no cover
    def _read_unicode(self, n):# pragma: no cover
        return 'Unicode string'[:n]# pragma: no cover
    def _read_string(self, n):# pragma: no cover
        return 'String'[:n]# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
n = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
self.read = self._read_unicode if self._is_unicode else self._read_string
_l_(7358)
aux = self.read(n).lstrip()
_l_(7359)
exit(aux)
