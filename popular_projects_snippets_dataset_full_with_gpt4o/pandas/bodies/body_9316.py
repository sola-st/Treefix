# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH:
arr = pd.arrays.StringArray._from_sequence([nulls_fixture] * 2)
result = Categorical(arr)
assert arr.dtype == result.categories.dtype
expected = Categorical(Series([pd.NA, pd.NA], dtype=arr.dtype))
tm.assert_categorical_equal(result, expected)
