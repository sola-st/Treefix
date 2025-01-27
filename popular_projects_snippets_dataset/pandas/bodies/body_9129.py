# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_algos.py
# GH2003
cat = pd.Categorical(["a", "b", np.nan])

result = cat.isin(["a", np.nan])
expected = np.array([True, False, True], dtype=bool)
tm.assert_numpy_array_equal(expected, result)

result = cat.isin(["a", "c"])
expected = np.array([True, False, False], dtype=bool)
tm.assert_numpy_array_equal(expected, result)
