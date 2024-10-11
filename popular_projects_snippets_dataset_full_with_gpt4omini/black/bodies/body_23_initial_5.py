from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), { 'current_line': MagicMock() })() # pragma: no cover
leaf = 'mocked_leaf' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if not self.current_line.bracket_tracker.any_open_brackets():
    _l_(5062)

    aux = self.line()
    _l_(5061)
    exit(aux)
aux = self.visit_default(leaf)
_l_(5063)
exit(aux)
