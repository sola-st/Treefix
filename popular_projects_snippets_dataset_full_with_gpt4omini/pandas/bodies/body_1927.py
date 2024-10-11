# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 13083
pi = period_range(start="2000", freq="D", periods=10)
s = Series(range(len(pi)), index=pi)
expected = s.to_timestamp().resample(freq).ohlc().to_period(freq)

# timestamp-based resampling doesn't include all sub-periods
# of the last original period, so extend accordingly:
new_index = period_range(start="2000", freq=freq, periods=period_mult * len(pi))
expected = expected.reindex(new_index)
result = s.resample(freq, kind=kind).ohlc()
tm.assert_frame_equal(result, expected)
