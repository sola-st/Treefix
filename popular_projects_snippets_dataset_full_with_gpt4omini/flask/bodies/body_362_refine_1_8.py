from collections import UserDict # pragma: no cover

class Mock(UserDict): pass # pragma: no cover
self = Mock() # pragma: no cover
key = 'sample_key' # pragma: no cover

from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def __getitem__(self, key): return 'value_for_' + key # pragma: no cover
self = Mock() # pragma: no cover
self['sample_key'] = 'value_for_sample_key' # pragma: no cover
key = 'sample_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
