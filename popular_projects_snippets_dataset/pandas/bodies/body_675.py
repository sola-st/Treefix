# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
stamp = datetime(2363, 10, 4)  # Enterprise-D launch date
if dtype == "timedelta64[ns]":
    stamp = stamp - datetime(1970, 1, 1)
arr = np.array([stamp], dtype=object)

out = lib.maybe_convert_objects(
    arr, convert_datetime=True, convert_timedelta=True
)
# no OutOfBoundsDatetime/OutOfBoundsTimedeltas
tm.assert_numpy_array_equal(out, arr)
