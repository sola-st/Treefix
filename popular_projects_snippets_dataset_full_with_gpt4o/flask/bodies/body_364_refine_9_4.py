key = 'example_key' # pragma: no cover
default = 'default_value' # pragma: no cover
self = type('Mock', (object,), {'accessed': True, 'setdefault': lambda self, key, default: None})() # pragma: no cover

class Base:# pragma: no cover
    def setdefault(self, key, default):# pragma: no cover
        return f'Setting {key} to default {default}'# pragma: no cover
 # pragma: no cover
class Mock(Base):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.accessed = False# pragma: no cover
 # pragma: no cover
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
