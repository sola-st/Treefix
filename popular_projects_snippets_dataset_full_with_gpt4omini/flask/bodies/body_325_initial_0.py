from typing import Any, Dict # pragma: no cover

class Mock: pass # pragma: no cover
self = type('MockSelf', (Mock,), {'_method_route': lambda method, rule, options: f'Executed {method} on {rule} with options {options}'})() # pragma: no cover
rule = '/example/route' # pragma: no cover
options = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Shortcut for :meth:`route` with ``methods=["DELETE"]``.

        .. versionadded:: 2.0
        """
aux = self._method_route("DELETE", rule, options)
_l_(9659)
exit(aux)
