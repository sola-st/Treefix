# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([pd.NaT, pd.NaT], dtype=object)
out = lib.maybe_convert_objects(
    arr, convert_datetime=True, convert_timedelta=True
)
# no dtype_if_all_nat passed -> we dont guess
tm.assert_numpy_array_equal(out, arr)

out = lib.maybe_convert_objects(
    arr,
    convert_datetime=True,
    convert_timedelta=True,
    dtype_if_all_nat=np.dtype("timedelta64[ns]"),
)
exp = np.array(["NaT", "NaT"], dtype="timedelta64[ns]")
tm.assert_numpy_array_equal(out, exp)

out = lib.maybe_convert_objects(
    arr,
    convert_datetime=True,
    convert_timedelta=True,
    dtype_if_all_nat=np.dtype("datetime64[ns]"),
)
exp = np.array(["NaT", "NaT"], dtype="datetime64[ns]")
tm.assert_numpy_array_equal(out, exp)
