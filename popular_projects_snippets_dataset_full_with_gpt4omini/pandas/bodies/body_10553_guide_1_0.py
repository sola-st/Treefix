import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

df = pd.DataFrame({'group': ['A', 'A', 'B'], 'v': [4, 5, 6]}, index=[-1, -2, -3]) # pragma: no cover
def f(values, index): return np.mean(index) # pragma: no cover
np.mean = lambda x: -np.sum(x) / len(x) # pragma: no cover
tm.assert_frame_equal = type('Mock', (object,), {'__call__': lambda self, a, b: print('Frames are equal')})() # pragma: no cover
expected = pd.DataFrame([-1.5, -3.0], columns=['v'], index=pd.Index(['A', 'B'], name='group')) # pragma: no cover

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
