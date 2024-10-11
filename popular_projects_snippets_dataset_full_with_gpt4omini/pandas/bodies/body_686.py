# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH14956
arr = np.array([datetime(2015, 1, 1, tzinfo=pytz.utc), 1], dtype=object)
result = lib.maybe_convert_objects(arr, convert_datetime=True)
tm.assert_numpy_array_equal(result, arr)
