from typing import Dict, Any # pragma: no cover

class Mock(dict): # pragma: no cover
    def get(self, key, default): # pragma: no cover
        return []  # Simulate a case that will raise IndexError when accessing [-1] # pragma: no cover
mock_dict = Mock() # pragma: no cover
key = 'some_key' # pragma: no cover
def_val = 'default_value' # pragma: no cover

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
