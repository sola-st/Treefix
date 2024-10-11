from flask import Flask, request # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = app.test_client() # pragma: no cover
rule = '/example' # pragma: no cover
options = {} # pragma: no cover
self._method_route = type('Mock', (object,), {'__call__': lambda self, method, rule, options: (method, rule, options)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["DELETE"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("DELETE", rule, options)
_l_(9659)
exit(aux)
