import pandas as pd # pragma: no cover

ddof = 1 # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'c'  # or 'python' based on preference # pragma: no cover
engine_kwargs = {'skipna': True} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/window/expanding.py
from l3.Runtime import _l_
aux = super().var(
    ddof=ddof,
    numeric_only=numeric_only,
    engine=engine,
    engine_kwargs=engine_kwargs,
)
_l_(9386)
exit(aux)
