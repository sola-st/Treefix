src = None # pragma: no cover
verbose = True # pragma: no cover
quiet = False # pragma: no cover
msg = 'No source provided' # pragma: no cover
def out(message): print(message) # pragma: no cover
ctx = type('Mock', (object,), {'exit': lambda self, code: print(f'Exiting with code {code}')} )() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""
    Exit if there is no `src` provided for formatting
    """
if not src:
    _l_(15962)

    if verbose or not quiet:
        _l_(15960)

        out(msg)
        _l_(15959)
    ctx.exit(0)
    _l_(15961)
