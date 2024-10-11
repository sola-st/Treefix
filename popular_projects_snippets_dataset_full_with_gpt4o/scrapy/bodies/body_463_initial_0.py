self = type('Mock', (object,), {# pragma: no cover
    '_read_unicode': lambda self, x: f'unicode string of length {x}',# pragma: no cover
    '_read_string': lambda self, x: f'string of length {x}',# pragma: no cover
    '_is_unicode': True,# pragma: no cover
})() # pragma: no cover
n = 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
self.read = self._read_unicode if self._is_unicode else self._read_string
_l_(18259)
aux = self.read(n).lstrip()
_l_(18260)
exit(aux)
