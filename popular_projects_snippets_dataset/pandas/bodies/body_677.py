# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
obj = np.timedelta64("NaT", "ns")
arr = np.array([obj], dtype=object)
assert arr[0] is obj

result = lib.maybe_convert_objects(arr, convert_timedelta=True)

expected = np.array([obj], dtype="m8[ns]")
tm.assert_numpy_array_equal(result, expected)
