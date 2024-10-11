# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_np_datetime.py
arr = np.array([-1500, 1500], dtype="M8[ns]")
dtype = np.dtype("M8[us]")

msg = "Cannot losslessly cast '-1500 ns' to us"
with pytest.raises(ValueError, match=msg):
    astype_overflowsafe(arr, dtype, round_ok=False)

result = astype_overflowsafe(arr, dtype, round_ok=True)
expected = arr.astype(dtype)
tm.assert_numpy_array_equal(result, expected)
