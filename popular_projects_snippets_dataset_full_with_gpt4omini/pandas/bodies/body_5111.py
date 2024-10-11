# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")
other = pd.to_datetime(["2000-01-01"]).values

expected = pd.to_datetime(["2000-01-02"]).values
tm.assert_numpy_array_equal(td + other, expected)
tm.assert_numpy_array_equal(other + td, expected)

expected = pd.to_datetime(["1999-12-31"]).values
tm.assert_numpy_array_equal(-td + other, expected)
tm.assert_numpy_array_equal(other - td, expected)
