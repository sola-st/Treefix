# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")

arr = np.array([td], dtype=object)
result = arr / td
expected = np.array([1], dtype=np.float64)
tm.assert_numpy_array_equal(result, expected)

arr = np.array([None])
result = arr / td
expected = np.array([np.nan])
tm.assert_numpy_array_equal(result, expected)

arr = np.array([np.nan], dtype=object)
msg = r"unsupported operand type\(s\) for /: 'float' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    arr / td

arr = np.array([np.nan], dtype=np.float64)
msg = "cannot use operands with types dtype"
with pytest.raises(TypeError, match=msg):
    arr / td
