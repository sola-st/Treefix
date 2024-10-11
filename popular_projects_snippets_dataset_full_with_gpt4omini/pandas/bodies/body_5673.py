# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = ["bar"]
data = ["foo"] * 2 + ["bar"] * 3

ser = Series(data, dtype=dt)
exp = Series(exp, dtype=dt)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
