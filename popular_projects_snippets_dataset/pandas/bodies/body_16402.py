# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
# regression test for GitHub issue #6439
# make sure that the ordering on datetimeindex is consistent
x = date_range("2000-01-01", periods=2)
result1, result2 = (Index(y).day for y in cartesian_product([x, x]))
expected1 = Index([1, 1, 2, 2], dtype=np.int32)
expected2 = Index([1, 2, 1, 2], dtype=np.int32)
tm.assert_index_equal(result1, expected1)
tm.assert_index_equal(result2, expected2)
