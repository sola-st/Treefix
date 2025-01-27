# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
dti = pd.date_range("2016-01-01", periods=6, tz="US/Pacific")
arr = np.array(dti, dtype=object).reshape(3, 2)
if order == "F":
    arr = arr.T

res = _sequence_to_dt64ns(arr)
expected = _sequence_to_dt64ns(arr.ravel())

tm.assert_numpy_array_equal(res[0].ravel(), expected[0])
assert res[1] == expected[1]
assert res[2] == expected[2]

res = DatetimeArray._from_sequence(arr)
expected = DatetimeArray._from_sequence(arr.ravel()).reshape(arr.shape)
tm.assert_datetime_array_equal(res, expected)
