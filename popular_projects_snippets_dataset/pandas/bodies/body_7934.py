# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# without method we aren't checking inequalities, so get all-missing
#  but do not raise
dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")

other = non_comparable_idx

res = pi[:-1].get_indexer(other)
expected = -np.ones(other.shape, dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
