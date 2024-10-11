import weakref # pragma: no cover

class MockApp: pass# pragma: no cover
app = MockApp() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._app = None # pragma: no cover
weakref.proxy = weakref.ref # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
self._app = weakref.proxy(app)
_l_(9640)
