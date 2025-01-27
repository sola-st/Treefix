# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
tz = tz_naive_fixture

dta = date_range("1970-01-01", freq="h", periods=5, tz=tz)._data

other = np.array([0, 1, 2, dta[3], Timedelta(days=1)])
result = dta == other
expected = np.array([False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)

result = dta != other
tm.assert_numpy_array_equal(result, ~expected)

msg = "Invalid comparison between|Cannot compare type|not supported between"
with pytest.raises(TypeError, match=msg):
    dta < other
with pytest.raises(TypeError, match=msg):
    dta > other
with pytest.raises(TypeError, match=msg):
    dta <= other
with pytest.raises(TypeError, match=msg):
    dta >= other
