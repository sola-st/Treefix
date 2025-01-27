# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# https://github.com/pandas-dev/pandas/issues/17981
c = Categorical(["a", "b"])
result = c.rename_categories(Series([0, 1], index=["a", "b"]))
expected = Categorical([0, 1])
tm.assert_categorical_equal(result, expected)
