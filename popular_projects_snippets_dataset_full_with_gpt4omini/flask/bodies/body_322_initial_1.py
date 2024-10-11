from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = app # pragma: no cover
rule = '/mock_route' # pragma: no cover
options = {} # pragma: no cover
self._method_route = type('Mock', (object,), {'__call__': lambda self, method, rule, options: f'Route {method} for {rule} with options {options}'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["GET"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("GET", rule, options)
_l_(8237)
exit(aux)
