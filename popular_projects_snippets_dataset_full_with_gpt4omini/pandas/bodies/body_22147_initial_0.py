import numpy as np # pragma: no cover
def func(g, *args, **kwargs): return g(*args, **kwargs) # pragma: no cover

g = lambda x: x + 1 # pragma: no cover
args = (2,) # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
from l3.Runtime import _l_
with np.errstate(all="ignore"):
    _l_(6655)

    aux = func(g, *args, **kwargs)
    _l_(6654)
    exit(aux)
