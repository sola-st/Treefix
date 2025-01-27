# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#38729/GH#38742
from l3.Runtime import _l_
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
_l_(19031)
arr = pd.array([7, pd.NA, 9])
_l_(19032)
ser = Series(arr)
_l_(19033)
mask = np.ones(df.shape, dtype=bool)
_l_(19034)
mask[1, :] = False
_l_(19035)

# TODO: ideally we would get Int64 instead of object
result = df.where(mask, ser, axis=0)
_l_(19036)
expected = DataFrame({"A": [1, pd.NA, 3], "B": [4, pd.NA, 6]}).astype(object)
_l_(19037)
tm.assert_frame_equal(result, expected)
_l_(19038)

ser2 = Series(arr[:2], index=["A", "B"])
_l_(19039)
expected = DataFrame({"A": [1, 7, 3], "B": [4, pd.NA, 6]})
_l_(19040)
expected["B"] = expected["B"].astype(object)
_l_(19041)
result = df.where(mask, ser2, axis=1)
_l_(19042)
tm.assert_frame_equal(result, expected)
_l_(19043)
