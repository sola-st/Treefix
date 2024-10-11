import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

date_range = pd.date_range # pragma: no cover
Timestamp = pd.Timestamp # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
np = np # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': staticmethod(lambda df1, df2: None)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# gh-17105

# insert a duplicate element to the index
from l3.Runtime import _l_
trange = date_range(
    start=Timestamp(year=2017, month=1, day=1),
    end=Timestamp(year=2017, month=1, day=5),
)
_l_(10639)

trange = trange.insert(loc=5, item=Timestamp(year=2017, month=1, day=5))
_l_(10640)

df = DataFrame(0, index=trange, columns=["A", "B"])
_l_(10641)
bool_idx = np.array([False, False, False, False, False, True])
_l_(10642)

# assignment
df.loc[trange[bool_idx], "A"] = 6
_l_(10643)

expected = DataFrame(
    {"A": [0, 0, 0, 0, 6, 6], "B": [0, 0, 0, 0, 0, 0]}, index=trange
)
_l_(10644)
tm.assert_frame_equal(df, expected)
_l_(10645)

# in-place
df = DataFrame(0, index=trange, columns=["A", "B"])
_l_(10646)
df.loc[trange[bool_idx], "A"] += 6
_l_(10647)
tm.assert_frame_equal(df, expected)
_l_(10648)
