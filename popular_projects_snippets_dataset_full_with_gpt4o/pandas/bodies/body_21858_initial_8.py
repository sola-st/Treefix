type # pragma: no cover

ddof = 1 # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'numpy' # pragma: no cover
engine_kwargs = {'optimize': True} # pragma: no cover
super = type('Mock', (object,), {'var': lambda self, ddof, numeric_only, engine, engine_kwargs: 'mock_exit'})() # pragma: no cover

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
