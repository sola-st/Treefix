self = type('Mock', (object,), {'current_line': type('Mock', (object,), {'bracket_tracker': type('Mock', (object,), {'any_open_brackets': lambda: False})}), 'line': lambda: 'Line called', 'visit_default': lambda x: 'Default visit'})() # pragma: no cover
leaf = 'SomeLeafValue' # pragma: no cover

leaf = 'SomeLeafValue' # pragma: no cover

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
