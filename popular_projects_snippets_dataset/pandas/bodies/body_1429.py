# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# range can cause an indexing error
# GH 11652
s = Series(index=range(size), dtype=np.float64)
s.loc[range(1)] = 42
tm.assert_series_equal(s.loc[range(1)], Series(42.0, index=[0]))

s.loc[range(2)] = 43
tm.assert_series_equal(s.loc[range(2)], Series(43.0, index=[0, 1]))
