import collections # pragma: no cover
import typing # pragma: no cover

class Mock(dict):# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'value_of_' + key# pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
