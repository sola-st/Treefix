from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
rule = '/example' # pragma: no cover
options = {} # pragma: no cover
self._method_route = lambda method, rule, options: 'Routed' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["GET"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("GET", rule, options)
_l_(19365)
exit(aux)
