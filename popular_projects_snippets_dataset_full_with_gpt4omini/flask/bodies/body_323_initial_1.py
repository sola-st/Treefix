from flask import Flask, request # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._method_route = lambda method, rule, options: f'Route method: {method}, Rule: {rule}, Options: {options}' # pragma: no cover
rule = '/example' # pragma: no cover
options = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["POST"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("POST", rule, options)
_l_(8256)
exit(aux)
