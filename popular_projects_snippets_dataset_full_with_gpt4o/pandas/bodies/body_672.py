# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH27438
arr = np.array(
    [np.datetime64("2000-01-01"), np.timedelta64(1, "s")], dtype=object
)
exp = arr.copy()
out = lib.maybe_convert_objects(
    arr, convert_datetime=True, convert_timedelta=True
)
tm.assert_numpy_array_equal(out, exp)

arr = np.array([pd.NaT, np.timedelta64(1, "s")], dtype=object)
exp = np.array([np.timedelta64("NaT"), np.timedelta64(1, "s")], dtype="m8[ns]")
out = lib.maybe_convert_objects(
    arr, convert_datetime=True, convert_timedelta=True
)
tm.assert_numpy_array_equal(out, exp)

# with convert_timedelta=True, the nan is a valid NA value for td64
arr = np.array([np.timedelta64(1, "s"), np.nan], dtype=object)
exp = exp[::-1]
out = lib.maybe_convert_objects(
    arr, convert_datetime=True, convert_timedelta=True
)
tm.assert_numpy_array_equal(out, exp)
