# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
# GH#35530
arr = np.array([0], dtype=np.int64)
arr.setflags(write=False)
result = tz_convert_from_utc(arr, UTC)
tm.assert_numpy_array_equal(result, arr)
