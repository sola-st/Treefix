# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")

other = np.array([td.to_timedelta64()])
expected = np.array([Timedelta("2 Days").to_timedelta64()])

result = td + other
tm.assert_numpy_array_equal(result, expected)
result = other + td
tm.assert_numpy_array_equal(result, expected)

result = td - other
tm.assert_numpy_array_equal(result, expected * 0)
result = other - td
tm.assert_numpy_array_equal(result, expected * 0)
