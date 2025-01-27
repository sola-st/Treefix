# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
dtype = CategoricalDtype(list("abc"), ordered)
expected_categories = dtype.categories
expected_ordered = dtype.ordered
result = dtype.update_dtype("category")
tm.assert_index_equal(result.categories, expected_categories)
assert result.ordered is expected_ordered
