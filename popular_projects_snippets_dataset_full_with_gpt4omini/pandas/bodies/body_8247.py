# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# GH#22458 : argument 'n' was deprecated in favor of 'periods'
idx = date_range(start=START, end=END, periods=3)
tm.assert_index_equal(idx.shift(periods=0), idx)
tm.assert_index_equal(idx.shift(0), idx)
