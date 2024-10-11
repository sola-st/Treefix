# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22074
dti = date_range("2000-01-01", periods=10, tz="Asia/Tokyo")

other = dti.astype("O")

result = dti == other
expected = np.array([True] * 10)
tm.assert_numpy_array_equal(result, expected)

other = dti.tz_localize(None)
result = dti != other
tm.assert_numpy_array_equal(result, expected)

other = np.array(list(dti[:5]) + [Timedelta(days=1)] * 5)
result = dti == other
expected = np.array([True] * 5 + [False] * 5)
tm.assert_numpy_array_equal(result, expected)
msg = ">=' not supported between instances of 'Timestamp' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    dti >= other
