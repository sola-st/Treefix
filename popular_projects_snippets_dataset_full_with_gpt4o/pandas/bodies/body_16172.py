# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH12723
ser = Series([0, 1, np.nan, 3, 4, 5])

exp = ser.fillna(0).add(2)
res = ser.add(2, fill_value=0)
tm.assert_series_equal(res, exp)
