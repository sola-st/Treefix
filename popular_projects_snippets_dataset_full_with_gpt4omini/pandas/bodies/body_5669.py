# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 15714
exp_single = [1]
data_single = [1]

exp_multi = [1]
data_multi = [1, 1]

ser = Series(data_single, dtype=dt)
exp = Series(exp_single, dtype=dt)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)

ser = Series(data_multi, dtype=dt)
exp = Series(exp_multi, dtype=dt)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
