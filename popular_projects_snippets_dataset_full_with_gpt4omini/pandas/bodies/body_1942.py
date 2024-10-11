# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH 33498
# check that the timedelta bins does not contains an extra bin
idx = timedelta_range(start=start, end=end, freq=freq)
s = Series(np.arange(len(idx)), index=idx)
result = s.resample(resample_freq).min()
expected_index = timedelta_range(freq=resample_freq, start=start, end=end)
tm.assert_index_equal(result.index, expected_index)
assert result.index.freq == expected_index.freq
assert not np.isnan(result[-1])
