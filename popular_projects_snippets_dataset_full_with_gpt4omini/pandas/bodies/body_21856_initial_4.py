import pandas as pd # pragma: no cover

numeric_only = True # pragma: no cover
engine = 'numpy' # pragma: no cover
engine_kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/window/expanding.py
from l3.Runtime import _l_
aux = super().median(
    numeric_only=numeric_only,
    engine=engine,
    engine_kwargs=engine_kwargs,
)
_l_(10492)
exit(aux)
