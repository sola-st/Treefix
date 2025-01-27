# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
c = Categorical(["a", "b", np.nan])
result = c._set_dtype(CategoricalDtype(["a", "c"]))
tm.assert_numpy_array_equal(result.codes, np.array([0, -1, -1], dtype="int8"))
