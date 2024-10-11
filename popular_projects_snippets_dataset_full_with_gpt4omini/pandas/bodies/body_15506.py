# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_repeat.py
ser = Series(np.random.randn(3), index=["a", "b", "c"])

reps = ser.repeat(5)
exp = Series(ser.values.repeat(5), index=ser.index.values.repeat(5))
tm.assert_series_equal(reps, exp)

to_rep = [2, 3, 4]
reps = ser.repeat(to_rep)
exp = Series(ser.values.repeat(to_rep), index=ser.index.values.repeat(to_rep))
tm.assert_series_equal(reps, exp)
