_out = lambda msg, nl=True, **kwargs: print(msg, end='\n' if nl else '') # pragma: no cover
message = 'Hello, World!' # pragma: no cover
nl = True # pragma: no cover
styles = {'style': 'bold'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
_out(message, nl=nl, **styles)
_l_(17621)
