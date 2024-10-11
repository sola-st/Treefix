# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp_single = [1]
data_single = [1] * 5 + [2] * 3

exp_multi = [1, 3]
data_multi = [1] * 5 + [2] * 3 + [3] * 5

ser = Series(data_single, dtype=dt)
exp = Series(exp_single, dtype=dt)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)

ser = Series(data_multi, dtype=dt)
exp = Series(exp_multi, dtype=dt)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
