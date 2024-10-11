ddof = 1 # pragma: no cover
numeric_only = False # pragma: no cover
engine = 'numpy' # pragma: no cover
engine_kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/window/expanding.py
from l3.Runtime import _l_
aux = super().var(
    ddof=ddof,
    numeric_only=numeric_only,
    engine=engine,
    engine_kwargs=engine_kwargs,
)
_l_(19689)
exit(aux)
