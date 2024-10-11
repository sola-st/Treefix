from collections import defaultdict # pragma: no cover

class Mock(dict): # pragma: no cover
    def get(self, key, def_val): # pragma: no cover
        return self.get(key, def_val) if key in self else def_val # pragma: no cover
 # pragma: no cover
mock_instance = Mock() # pragma: no cover
mock_instance['test'] = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
try:
    _l_(6763)

    aux = super().get(key, def_val)[-1]
    _l_(6760)
    exit(aux)
except IndexError:
    _l_(6762)

    aux = None
    _l_(6761)
    exit(aux)
