from pandas import DataFrame # pragma: no cover
from numpy import median # pragma: no cover

numeric_only = False # pragma: no cover
engine = 'default' # pragma: no cover
engine_kwargs = {} # pragma: no cover
super = type('Mock', (object,), {'median': lambda self, numeric_only, engine, engine_kwargs: 42}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/window/expanding.py
from l3.Runtime import _l_
aux = super().median(
    numeric_only=numeric_only,
    engine=engine,
    engine_kwargs=engine_kwargs,
)
_l_(21653)
exit(aux)
