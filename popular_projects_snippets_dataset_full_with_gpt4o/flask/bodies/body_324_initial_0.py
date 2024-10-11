from typing import Any, Dict # pragma: no cover

self = type('Mock', (object,), {'_method_route': lambda self, method, rule, options: 0})() # pragma: no cover
rule = '/api/resource' # pragma: no cover
options = {'option1': 'value1'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["PUT"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("PUT", rule, options)
_l_(22600)
exit(aux)
