# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
cat = Categorical(np.array(["foo", (0, 1), 3, (0, 1)], dtype=object))

result = cat == "foo"
expected = np.array([True, False, False, False], dtype=bool)
tm.assert_numpy_array_equal(result, expected)

result = cat == (0, 1)
expected = np.array([False, True, False, True], dtype=bool)
tm.assert_numpy_array_equal(result, expected)

result = cat != (0, 1)
tm.assert_numpy_array_equal(result, ~expected)
