from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (), {'current_line': MagicMock(bracket_tracker=MagicMock(any_open_brackets=MagicMock(return_value=False)))})() # pragma: no cover
leaf = 'sample_leaf' # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (), {'current_line': MagicMock(bracket_tracker=MagicMock(any_open_brackets=MagicMock(return_value=False))), 'line': MagicMock(return_value=42), 'visit_default': MagicMock(return_value='default_action')})() # pragma: no cover
leaf = 'sample_leaf' # pragma: no cover

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
