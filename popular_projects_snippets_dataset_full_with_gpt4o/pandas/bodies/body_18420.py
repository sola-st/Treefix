# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
tz = tz_naive_fixture
dti = date_range("2016-01-01", periods=2, tz=tz)
if tz is not None:
    if isinstance(other, np.datetime64):
        # no tzaware version available
        exit()
    other = localize_pydatetime(other, dti.tzinfo)

result = dti == other
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = dti > other
expected = np.array([False, True])
tm.assert_numpy_array_equal(result, expected)

result = dti >= other
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)

result = dti < other
expected = np.array([False, False])
tm.assert_numpy_array_equal(result, expected)

result = dti <= other
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)
