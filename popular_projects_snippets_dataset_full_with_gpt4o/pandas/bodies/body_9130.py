# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_algos.py
s = pd.Categorical(["a", "b"])
expected = np.array([False, False], dtype=bool)

result = s.isin(empty)
tm.assert_numpy_array_equal(expected, result)
