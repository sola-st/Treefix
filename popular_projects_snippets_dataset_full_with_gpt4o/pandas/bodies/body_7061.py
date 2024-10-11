# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
dtype = CategoricalDtype(categories, ordered=ordered)

idx = CategoricalIndex(data, dtype=dtype)
expected = CategoricalIndex(expected_data, dtype=dtype)
tm.assert_index_equal(idx.unique(), expected)
