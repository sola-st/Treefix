from werkzeug.wrappers import Request, Response # pragma: no cover
from werkzeug.test import EnvironBuilder # pragma: no cover

kwargs = {} # pragma: no cover
self = type('Mock', (object,), {'_copy_environ': lambda self, env: env.copy(), 'application': 'my_app'})() # pragma: no cover
EnvironBuilder = type('MockEnvironBuilder', (object,), {'__init__': lambda self, app, *args, **kwargs: None, 'get_request': lambda self: Request(environ={}),'close': lambda self: None}) # pragma: no cover
args = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
kwargs["environ_base"] = self._copy_environ(kwargs.get("environ_base", {}))
_l_(8812)
builder = EnvironBuilder(self.application, *args, **kwargs)
_l_(8813)

try:
    _l_(8817)

    aux = builder.get_request()
    _l_(8814)
    exit(aux)
finally:
    _l_(8816)

    builder.close()
    _l_(8815)
