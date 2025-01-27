# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
idx = Index([2, np.nan, 2, 1], name="my_index")
expected = Index([2, np.nan, 1], name="my_index")
result = idx.unique()
tm.assert_index_equal(result, expected)
