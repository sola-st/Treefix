# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = ["1", "-3.14", "7"]
res = to_numeric(ser)

expected = np.array([1, -3.14, 7])
tm.assert_numpy_array_equal(res, expected)
