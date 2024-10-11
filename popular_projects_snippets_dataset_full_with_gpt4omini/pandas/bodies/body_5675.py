# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series(["-1 days", "0 days", "1 days"], dtype="timedelta64[ns]")
ser = Series(["1 days", "-1 days", "0 days"], dtype="timedelta64[ns]")
tm.assert_extension_array_equal(algos.mode(ser.values), exp._values)
tm.assert_series_equal(ser.mode(), exp)

exp = Series(["2 min", "1 day"], dtype="timedelta64[ns]")
ser = Series(
    ["1 day", "1 day", "-1 day", "-1 day 2 min", "2 min", "2 min"],
    dtype="timedelta64[ns]",
)
tm.assert_extension_array_equal(algos.mode(ser.values), exp._values)
tm.assert_series_equal(ser.mode(), exp)
