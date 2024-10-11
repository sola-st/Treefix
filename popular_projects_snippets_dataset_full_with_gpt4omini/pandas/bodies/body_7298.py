# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_ops.py
# GH#11018
idx = timedelta_range("1", freq=freq_sample, periods=10)
result = TimedeltaIndex(idx.asi8, freq="infer")
tm.assert_index_equal(idx, result)
assert result.freq == freq_sample
