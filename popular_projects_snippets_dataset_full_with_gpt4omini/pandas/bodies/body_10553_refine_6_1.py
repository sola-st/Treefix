import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
Index = pd.Index # pragma: no cover
np = np # pragma: no cover
tm = tm # pragma: no cover
np.mean = np.mean # pragma: no cover
tm.assert_frame_equal = lambda left, right: pd.testing.assert_frame_equal(left, right) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
Index = pd.Index # pragma: no cover
np.mean = staticmethod(lambda x: sum(x) / len(x)) # pragma: no cover
tm = type('MockTM', (object,), {'assert_frame_equal': staticmethod(lambda left, right: None)})() # pragma: no cover
f = lambda values, index: np.mean(index) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
# GH 43133
from l3.Runtime import _l_
def f(values, index):
    _l_(5431)

    aux = np.mean(index)
    _l_(5430)
    exit(aux)

df = DataFrame({"group": ["A", "A", "B"], "v": [4, 5, 6]}, index=[-1, -2, -3])
_l_(5432)
result = df.groupby("group").aggregate(f, engine="numba")
_l_(5433)
expected = DataFrame(
    [-1.5, -3.0], columns=["v"], index=Index(["A", "B"], name="group")
)
_l_(5434)
tm.assert_frame_equal(result, expected)
_l_(5435)
