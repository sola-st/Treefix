self = type('Mock', (object,), {'_method_route': lambda self, method, rule, options: 'Mock Route'})() # pragma: no cover
rule = '/delete-resource' # pragma: no cover
options = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["DELETE"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("DELETE", rule, options)
_l_(20887)
exit(aux)
