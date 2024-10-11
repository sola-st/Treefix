import pandas as pd # pragma: no cover

numeric_only = True # pragma: no cover
engine = 'numba' # pragma: no cover
engine_kwargs = {} # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover

class MockDataFrame(DataFrame): # pragma: no cover
    def median(self, numeric_only=None, engine=None, engine_kwargs=None): # pragma: no cover
        return 0  # Mock return value # pragma: no cover
 # pragma: no cover
df = MockDataFrame() # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'numba' # pragma: no cover
engine_kwargs = {} # pragma: no cover
super = lambda: df # pragma: no cover

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
