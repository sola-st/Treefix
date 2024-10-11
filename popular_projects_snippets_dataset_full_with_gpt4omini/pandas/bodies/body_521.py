# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = CategoricalDtype(["a", "b", "c"])
tm.assert_index_equal(result.categories, pd.Index(["a", "b", "c"]))
assert result.ordered is False
