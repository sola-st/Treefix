# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series(["foo"])
ser = Series([1, "foo", "foo"])
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
