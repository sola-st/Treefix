import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

class MockCompute:  # Mock class for compute method # pragma: no cover
    def __init__(self): # pragma: no cover
        self.ctx = {(0, 0): 0.0, (1, 0): 1.0, (2, 0): 2.0} # pragma: no cover
 # pragma: no cover
class MockStyler:  # Mock class for Styler # pragma: no cover
    def background_gradient(self): # pragma: no cover
        return self # pragma: no cover
    def _compute(self): # pragma: no cover
        return MockCompute() # pragma: no cover
 # pragma: no cover
class MockDataFrame:  # Mock class for DataFrame # pragma: no cover
    def __init__(self, data): # pragma: no cover
        self.data = data # pragma: no cover
    @property # pragma: no cover
    def style(self): # pragma: no cover
        return MockStyler() # pragma: no cover
 # pragma: no cover
df1 = MockDataFrame([0, 1, 2]) # pragma: no cover
df2 = MockDataFrame([0, 1, 2]) # pragma: no cover
Series = lambda data, dtype=None: MockDataFrame(data) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# GH 28869
from l3.Runtime import _l_
df1 = Series(range(3)).to_frame()
_l_(10393)
df2 = Series(range(3), dtype="Int64").to_frame()
_l_(10394)
ctx1 = df1.style.background_gradient()._compute().ctx
_l_(10395)
ctx2 = df2.style.background_gradient()._compute().ctx
_l_(10396)
assert ctx2[(0, 0)] == ctx1[(0, 0)]
_l_(10397)
assert ctx2[(1, 0)] == ctx1[(1, 0)]
_l_(10398)
assert ctx2[(2, 0)] == ctx1[(2, 0)]
_l_(10399)
