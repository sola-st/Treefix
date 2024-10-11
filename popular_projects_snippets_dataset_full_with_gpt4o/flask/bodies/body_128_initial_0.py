self = type('Mock', (object,), {'shell_context_processors': []})() # pragma: no cover
f = lambda: 'test' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Registers a shell context processor function.

        .. versionadded:: 0.11
        """
self.shell_context_processors.append(f)
_l_(16646)
aux = f
_l_(16647)
exit(aux)
