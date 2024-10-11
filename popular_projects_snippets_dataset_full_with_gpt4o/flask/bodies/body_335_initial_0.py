self = type('Mock', (object,), {'template_context_processors': {None: []}})() # pragma: no cover
f = lambda: 'test function' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Registers a template context processor function."""
self.template_context_processors[None].append(f)
_l_(17706)
aux = f
_l_(17707)
exit(aux)
