import numpy as np # pragma: no cover

func = lambda *args, **kwargs: 0 # pragma: no cover
g = 0 # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
from l3.Runtime import _l_
with np.errstate(all="ignore"):
    _l_(18645)

    aux = func(g, *args, **kwargs)
    _l_(18644)
    exit(aux)
