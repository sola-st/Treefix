import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
Series = pd.Series # pragma: no cover
np = type('Mock', (object,), {'ones': np.ones})() # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': tm.assert_frame_equal})() # pragma: no cover
pd = type('Mock', (object,), {'array': pd.array, 'NA': pd.NA})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#38729/GH#38742
from l3.Runtime import _l_
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
_l_(8871)
arr = pd.array([7, pd.NA, 9])
_l_(8872)
ser = Series(arr)
_l_(8873)
mask = np.ones(df.shape, dtype=bool)
_l_(8874)
mask[1, :] = False
_l_(8875)

# TODO: ideally we would get Int64 instead of object
result = df.where(mask, ser, axis=0)
_l_(8876)
expected = DataFrame({"A": [1, pd.NA, 3], "B": [4, pd.NA, 6]}).astype(object)
_l_(8877)
tm.assert_frame_equal(result, expected)
_l_(8878)

ser2 = Series(arr[:2], index=["A", "B"])
_l_(8879)
expected = DataFrame({"A": [1, 7, 3], "B": [4, pd.NA, 6]})
_l_(8880)
expected["B"] = expected["B"].astype(object)
_l_(8881)
result = df.where(mask, ser2, axis=1)
_l_(8882)
tm.assert_frame_equal(result, expected)
_l_(8883)
