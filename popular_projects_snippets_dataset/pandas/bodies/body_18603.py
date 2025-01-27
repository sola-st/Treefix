# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_np_datetime.py
dtype = np.dtype("M8[ns]")

dt = np.datetime64("2262-04-05", "D")
arr = dt + np.arange(10, dtype="m8[D]")

# arr.astype silently overflows, so this
wrong = arr.astype(dtype)
roundtrip = wrong.astype(arr.dtype)
assert not (wrong == roundtrip).all()

msg = "Out of bounds nanosecond timestamp"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    astype_overflowsafe(arr, dtype)

# But converting to microseconds is fine, and we match numpy's results.
dtype2 = np.dtype("M8[us]")
result = astype_overflowsafe(arr, dtype2)
expected = arr.astype(dtype2)
tm.assert_numpy_array_equal(result, expected)
