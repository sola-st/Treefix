from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace( # pragma: no cover
    current_line=SimpleNamespace( # pragma: no cover
        bracket_tracker=SimpleNamespace( # pragma: no cover
            any_open_brackets=lambda: False # pragma: no cover
        ) # pragma: no cover
    ), # pragma: no cover
    line=lambda: 'line_executed', # pragma: no cover
    visit_default=lambda leaf: 'visit_default_executed' # pragma: no cover
) # pragma: no cover
leaf = None # pragma: no cover

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
