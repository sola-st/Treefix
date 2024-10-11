import pandas as pd # pragma: no cover

numeric_only = True # pragma: no cover
engine = 'numba' # pragma: no cover
engine_kwargs = {} # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockSeries:  # Mocking a Pandas Series# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
    def median(self, numeric_only=True, engine='python', engine_kwargs=None):# pragma: no cover
        return np.median(self.data) if numeric_only else np.mean(self.data)# pragma: no cover
# pragma: no cover
mock_series = MockSeries([1, 2, 3, 4, 5]) # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'python' # pragma: no cover
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
