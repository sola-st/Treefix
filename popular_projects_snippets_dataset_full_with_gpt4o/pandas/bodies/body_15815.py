# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
ser = Series(items)
exp = Series(Categorical(items))
res = ser.astype("category")
tm.assert_series_equal(res, exp)
