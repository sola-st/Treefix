# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
result = Series(
    ["a", "b"], dtype=CategoricalDtype(["a", "b", "c"], ordered=True)
)
assert is_categorical_dtype(result.dtype) is True
tm.assert_index_equal(result.cat.categories, Index(["a", "b", "c"]))
assert result.cat.ordered

result = Series(["a", "b"], dtype=CategoricalDtype(["b", "a"]))
assert is_categorical_dtype(result.dtype)
tm.assert_index_equal(result.cat.categories, Index(["b", "a"]))
assert result.cat.ordered is False

# GH 19565 - Check broadcasting of scalar with Categorical dtype
result = Series(
    "a", index=[0, 1], dtype=CategoricalDtype(["a", "b"], ordered=True)
)
expected = Series(
    ["a", "a"], index=[0, 1], dtype=CategoricalDtype(["a", "b"], ordered=True)
)
tm.assert_series_equal(result, expected)
