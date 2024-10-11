# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 23882 & 31809
s = Series(0, index=period_range(start, end, freq=start_freq))
s = s + np.arange(len(s))
result = s.resample(end_freq, offset=offset).mean()
result = result.to_timestamp(end_freq)

expected = s.to_timestamp().resample(end_freq, offset=offset).mean()
if end_freq == "M":
    # TODO: is non-tick the relevant characteristic? (GH 33815)
    expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
