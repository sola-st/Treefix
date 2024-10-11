import pandas as pd # pragma: no cover

ddof = 1 # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'c' if pd.__version__ >= '1.0.0' else 'python' # pragma: no cover
engine_kwargs = {'some_key': 'some_value'} # pragma: no cover

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
