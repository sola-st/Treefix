# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
# Just a basic smoke test. The EA interface tests exercise this
# more thoroughly.
x = PandasArray(np.array([1, 2, 3]))
result = x + x
expected = PandasArray(np.array([2, 4, 6]))
tm.assert_extension_array_equal(result, expected)
