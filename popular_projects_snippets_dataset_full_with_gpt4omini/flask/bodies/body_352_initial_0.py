from http import HTTPStatus # pragma: no cover
from werkzeug.wrappers import Request # pragma: no cover

kwargs = {} # pragma: no cover
self = type('MockSelf', (object,), {'_copy_environ': lambda self, x: x, 'application': 'mock_application'})() # pragma: no cover
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
