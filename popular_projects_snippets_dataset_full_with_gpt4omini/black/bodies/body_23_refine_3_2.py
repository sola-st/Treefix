from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'current_line': Mock()})() # pragma: no cover
leaf = Mock() # pragma: no cover
self.current_line.bracket_tracker = Mock() # pragma: no cover
self.current_line.bracket_tracker.any_open_brackets = Mock(return_value=False) # pragma: no cover
self.line = Mock(return_value='exiting_line') # pragma: no cover
self.visit_default = Mock(return_value='default_value') # pragma: no cover

from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'current_line': Mock()})() # pragma: no cover
leaf = Mock() # pragma: no cover
self.current_line.bracket_tracker = Mock() # pragma: no cover
self.current_line.bracket_tracker.any_open_brackets = Mock(return_value=False) # pragma: no cover
self.line = Mock(return_value='1') # pragma: no cover
self.visit_default = Mock(return_value='default_value') # pragma: no cover

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
