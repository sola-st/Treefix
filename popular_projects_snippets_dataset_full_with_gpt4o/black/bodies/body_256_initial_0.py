_out = print # pragma: no cover
message = 'Hello, World!' # pragma: no cover
nl = '\n' # pragma: no cover
styles = {'color': 'blue', 'font-weight': 'bold'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
_out(message, nl=nl, **styles)
_l_(17621)
