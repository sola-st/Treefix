# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series([0, 1, 2])
tm.assert_index_equal(s.index, Index(range(3)), exact=True)
