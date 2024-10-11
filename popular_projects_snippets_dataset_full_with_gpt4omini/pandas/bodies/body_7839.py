# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
idx = PeriodIndex([2000, 2007, 2007, 2009, 2009], freq="A-JUN")
expected = PeriodIndex([2000, 2007, 2009], freq="A-JUN")
tm.assert_index_equal(idx.unique(), expected)
assert idx.nunique() == 3
