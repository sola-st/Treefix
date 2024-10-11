from typing import Dict # pragma: no cover

message = 'An error occurred' # pragma: no cover
nl = True # pragma: no cover
styles = {'color': 'red', 'font-weight': 'bold'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
_err(message, nl=nl, **styles)
_l_(5522)
