import random # pragma: no cover

possible_slots = [1, 2, 3, 4] # pragma: no cover
self = type('Mock', (object,), {'_active_downloads': lambda self, slot: random.choice([True, False])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
aux = [(self._active_downloads(slot), slot) for slot in possible_slots]
_l_(16080)
exit(aux)
