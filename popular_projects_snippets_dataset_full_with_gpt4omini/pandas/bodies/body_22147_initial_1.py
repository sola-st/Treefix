import numpy as np # pragma: no cover
def func(g, *args, **kwargs): return g + sum(args) + sum(kwargs.values()) # pragma: no cover

g = 10 # pragma: no cover
args = (1, 2, 3) # pragma: no cover
kwargs = {'a': 4, 'b': 5} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
from l3.Runtime import _l_
with np.errstate(all="ignore"):
    _l_(6655)

    aux = func(g, *args, **kwargs)
    _l_(6654)
    exit(aux)
