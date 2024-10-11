# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
dti = date_range("2016-01-01", periods=3, tz=None)
dt64vals = dti.values

dtarr = tm.box_expected(dti, box_with_array)

expected = dtarr - dtarr
result = dtarr - dt64vals
tm.assert_equal(result, expected)
result = dt64vals - dtarr
tm.assert_equal(result, expected)
