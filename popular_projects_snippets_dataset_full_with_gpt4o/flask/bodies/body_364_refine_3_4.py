self = type('Mock', (object,), {'accessed': True})() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

class BaseClass:# pragma: no cover
    def setdefault(self, key, default):# pragma: no cover
        return {'example_key': 'example_existing_value'}.setdefault(key, default) # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    accessed = False # pragma: no cover
self = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover
default = 'example_default' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22601)
aux = super().setdefault(key, default)
_l_(22602)
exit(aux)
