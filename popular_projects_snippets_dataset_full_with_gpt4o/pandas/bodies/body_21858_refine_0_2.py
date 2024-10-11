ddof = 1 # pragma: no cover
numeric_only = False # pragma: no cover
engine = 'cython' # pragma: no cover
engine_kwargs = {'nopython': True} # pragma: no cover

ddof = 1 # pragma: no cover
numeric_only = False # pragma: no cover
engine = 'cython' # pragma: no cover
engine_kwargs = {'nopython': True} # pragma: no cover
class BaseClass:# pragma: no cover
    def var(self, ddof, numeric_only, engine, engine_kwargs):# pragma: no cover
        return 42 # pragma: no cover
class SubClass(BaseClass):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__() # pragma: no cover
instance = SubClass() # pragma: no cover

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
