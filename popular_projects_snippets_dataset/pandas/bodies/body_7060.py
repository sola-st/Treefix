# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

idx = CategoricalIndex(data, categories=categories, name="foo")
for keep, e in expected.items():
    tm.assert_numpy_array_equal(idx.duplicated(keep=keep), e)
    e = idx[~e]
    result = idx.drop_duplicates(keep=keep)
    tm.assert_index_equal(result, e)
