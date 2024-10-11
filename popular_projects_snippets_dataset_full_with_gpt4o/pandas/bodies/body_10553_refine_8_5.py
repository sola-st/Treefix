import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame, Index # pragma: no cover

np = type('Mock', (object,), {'mean': np.mean}) # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': pd.testing.assert_frame_equal}) # pragma: no cover

import numpy as np # pragma: no cover
from pandas import DataFrame, Index # pragma: no cover
import pandas.testing as tm # pragma: no cover

DataFrame = type('Mock', (object,), {'groupby': lambda *args, **kwargs: type('Mock', (object,), {'aggregate': lambda func, engine='numba': pd.DataFrame({"v": [-1.5, -3.0]}, index=pd.Index(["A", "B"], name="group"))})()}) # pragma: no cover

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
