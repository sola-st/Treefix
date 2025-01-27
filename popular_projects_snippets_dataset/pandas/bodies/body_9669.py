# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_astype.py
# We choose to ignore the sign and size of integers for
# Period/Datetime/Timedelta astype
arr = period_array(["2000", "2001", None], freq="D")

if np.dtype(dtype) != np.int64:
    with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
        arr.astype(dtype)
    exit()

result = arr.astype(dtype)
expected = arr._ndarray.view("i8")
tm.assert_numpy_array_equal(result, expected)
