# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#13514 change: {nan} - {nan} == {}
# (GH#6444, sorting of nans, is no longer an issue)
index1 = Index([1, np.nan, 2, 3])

result = index1.symmetric_difference(index2, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
