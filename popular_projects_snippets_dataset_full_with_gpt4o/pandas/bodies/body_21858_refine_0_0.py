ddof = 1 # pragma: no cover
numeric_only = False # pragma: no cover
engine = 'cython' # pragma: no cover
engine_kwargs = {'nopython': True} # pragma: no cover

class MockSuper(object): # pragma: no cover
    def var(self, ddof, numeric_only, engine, engine_kwargs): # pragma: no cover
        return 'mocked_var_call' # pragma: no cover
 # pragma: no cover
class Mock(MockSuper): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
ddof = 1 # pragma: no cover
numeric_only = False # pragma: no cover
engine = 'cython' # pragma: no cover
engine_kwargs = {'nopython': True} # pragma: no cover

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
