# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# GH#14811
dti = date_range(start="2016-10-21", end="2016-10-21", freq="BM")
result = dti.shift(1)
tm.assert_index_equal(result, dti)
