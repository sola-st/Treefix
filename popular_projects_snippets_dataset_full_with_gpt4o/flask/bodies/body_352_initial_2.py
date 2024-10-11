from werkzeug.test import EnvironBuilder # pragma: no cover
from werkzeug.wrappers import Request # pragma: no cover
import os # pragma: no cover

kwargs = {} # pragma: no cover
self = type('Mock', (object,), {'_copy_environ': lambda self, env: env.copy(), 'application': lambda environ, start_response: None})() # pragma: no cover
args = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
kwargs["environ_base"] = self._copy_environ(kwargs.get("environ_base", {}))
_l_(22922)
builder = EnvironBuilder(self.application, *args, **kwargs)
_l_(22923)

try:
    _l_(22927)

    aux = builder.get_request()
    _l_(22924)
    exit(aux)
finally:
    _l_(22926)

    builder.close()
    _l_(22925)
