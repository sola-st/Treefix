leaf = 'example_leaf' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.current_line = type('Mock', (object,), {'bracket_tracker': type('Mock', (object,), {'any_open_brackets': lambda: False})()})() # pragma: no cover
self.line = lambda: 'exiting due to no open brackets' # pragma: no cover
self.visit_default = lambda leaf: f'default visit for {leaf}' # pragma: no cover

leaf = 'example_leaf' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.current_line = type('Mock', (object,), {# pragma: no cover
  'bracket_tracker': type('Mock', (object,), {'any_open_brackets': lambda self: False})()# pragma: no cover
})() # pragma: no cover
self.line = lambda: 'exiting due to no open brackets' # pragma: no cover
self.visit_default = lambda leaf: f'default visit for {leaf}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if not self.current_line.bracket_tracker.any_open_brackets():
    _l_(16729)

    aux = self.line()
    _l_(16728)
    exit(aux)
aux = self.visit_default(leaf)
_l_(16730)
exit(aux)
