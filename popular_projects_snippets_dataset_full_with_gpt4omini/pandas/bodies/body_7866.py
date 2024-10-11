# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_shift.py
# GH #22458 : argument 'n' was deprecated in favor of 'periods'
idx = period_range(freq="A", start="1/1/2001", end="12/1/2009")
tm.assert_index_equal(idx.shift(periods=0), idx)
tm.assert_index_equal(idx.shift(0), idx)
