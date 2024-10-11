import weakref # pragma: no cover

app = type('MockApp', (object,), {})() # pragma: no cover
self = type('MockSelf', (object,), {'_app': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
self._app = weakref.proxy(app)
_l_(20794)
