leaf = 'dummy_leaf' # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
  'current_line': type('Mock', (object,), {'bracket_tracker': type('Mock', (object,), {# pragma: no cover
    'any_open_brackets': lambda: False# pragma: no cover
  })()})(),# pragma: no cover
  'line': lambda: 'line_info',# pragma: no cover
  'visit_default': lambda leaf: 'default_visit'# pragma: no cover
})() # pragma: no cover

leaf = 'dummy_leaf' # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
  'current_line': type('Mock', (object,), {# pragma: no cover
    'bracket_tracker': type('Mock', (object,), {# pragma: no cover
      'any_open_brackets': lambda self: False# pragma: no cover
    })()# pragma: no cover
  })(),# pragma: no cover
  'line': lambda: 'line_info',# pragma: no cover
  'visit_default': lambda leaf: 'default_visit'# pragma: no cover
})() # pragma: no cover

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
