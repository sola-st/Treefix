# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py
c = Categorical(["a", "b", "c"])
result = c._set_dtype(CategoricalDtype(["a", "b", "c"]))
tm.assert_categorical_equal(result, c)
