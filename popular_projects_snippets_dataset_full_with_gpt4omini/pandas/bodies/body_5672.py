# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = ["b"]
data = ["a"] * 2 + ["b"] * 3

ser = Series(data, dtype="c")
exp = Series(exp, dtype="c")
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
