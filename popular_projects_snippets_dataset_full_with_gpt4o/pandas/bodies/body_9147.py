# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py
c = Categorical(values, categories)
expected = Categorical(values, new_categories, ordered)
result = c._set_dtype(expected.dtype)
tm.assert_categorical_equal(result, expected)
