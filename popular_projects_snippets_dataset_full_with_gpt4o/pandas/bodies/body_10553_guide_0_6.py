import numpy as np # pragma: no cover
from pandas import DataFrame, Index # pragma: no cover
import pandas._testing as tm # pragma: no cover

class MockGroupBy: # pragma: no cover
    def aggregate(self, func, engine): # pragma: no cover
        index = [-1, -2] # pragma: no cover
        values = [4, 5] # pragma: no cover
        return DataFrame({"v": [func(values, index)]}, index=Index(["A"], name="group")) # pragma: no cover
 # pragma: no cover
DataFrame.groupby = lambda self, key: MockGroupBy() # pragma: no cover
df = DataFrame({"group": ["A", "A", "B"], "v": [4, 5, 6]}, index=[-1, -2, -3]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
# GH 43133
from l3.Runtime import _l_
def f(values, index):
    _l_(16117)

    aux = np.mean(index)
    _l_(16116)
    exit(aux)

df = DataFrame({"group": ["A", "A", "B"], "v": [4, 5, 6]}, index=[-1, -2, -3])
_l_(16118)
result = df.groupby("group").aggregate(f, engine="numba")
_l_(16119)
expected = DataFrame(
    [-1.5, -3.0], columns=["v"], index=Index(["A", "B"], name="group")
)
_l_(16120)
tm.assert_frame_equal(result, expected)
_l_(16121)
