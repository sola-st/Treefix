# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py
c = Categorical(["a", "b", "c"], ["d", "e"])
result = c._set_dtype(CategoricalDtype(["a", "b"]))
expected = Categorical([None, None, None], categories=["a", "b"])
tm.assert_categorical_equal(result, expected)
