# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#4134, buggy with timedeltas
rng = pd.date_range("2013", "2014")
s = Series(rng)
result1 = rng - offsets.Hour(1)
result2 = DatetimeIndex(s - np.timedelta64(100000000))
result3 = rng - np.timedelta64(100000000)
result4 = DatetimeIndex(s - offsets.Hour(1))

assert result1.freq == rng.freq
result1 = result1._with_freq(None)
tm.assert_index_equal(result1, result4)

assert result3.freq == rng.freq
result3 = result3._with_freq(None)
tm.assert_index_equal(result2, result3)
