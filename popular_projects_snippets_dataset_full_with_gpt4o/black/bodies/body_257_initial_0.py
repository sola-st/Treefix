_err = lambda message, nl, **styles: print(f"message: {message}, nl: {nl}, styles: {styles}") # pragma: no cover
message = 'This is an error message' # pragma: no cover
nl = '\n' # pragma: no cover
styles = {'color': 'red', 'bold': True} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
_err(message, nl=nl, **styles)
_l_(17237)
