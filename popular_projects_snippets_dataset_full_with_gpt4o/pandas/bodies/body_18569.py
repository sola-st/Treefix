# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
# see gh-4601
#
# These strings don't look like datetimes, so
# they shouldn't be attempted to be converted.
arr = np.array(data, dtype=object)
result, _ = tslib.array_to_datetime(arr, errors="ignore")

tm.assert_numpy_array_equal(result, arr)
