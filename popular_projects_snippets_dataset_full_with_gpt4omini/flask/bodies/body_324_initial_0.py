from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = app # pragma: no cover
rule = '/example' # pragma: no cover
options = {} # pragma: no cover
self._method_route = type('Mock', (object,), {'__call__': lambda self, method, rule, options: f'Called with {method}, {rule}, {options}'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["PUT"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("PUT", rule, options)
_l_(5332)
exit(aux)
