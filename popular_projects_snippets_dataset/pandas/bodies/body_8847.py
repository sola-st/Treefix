# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# arbitrary tz-naive DatetimeIndex
op = comparison_op

dti = pd.date_range("2016-01-1", freq="MS", periods=9, tz=None)
arr = DatetimeArray(dti)
assert arr.freq == dti.freq
assert arr.tz == dti.tz

right = dti

expected = np.ones(len(arr), dtype=bool)
if comparison_op.__name__ in ["ne", "gt", "lt"]:
    # for these the comparisons should be all-False
    expected = ~expected

result = op(arr, arr)
tm.assert_numpy_array_equal(result, expected)
for other in [
    right,
    np.array(right),
    list(right),
    tuple(right),
    right.astype(object),
]:
    result = op(arr, other)
    tm.assert_numpy_array_equal(result, expected)

    result = op(other, arr)
    tm.assert_numpy_array_equal(result, expected)
