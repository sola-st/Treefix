# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_ops.py
# GH 11018
idx = date_range("2011-01-01 09:00:00", freq=freq_sample, periods=10)
result = DatetimeIndex(idx.asi8, freq="infer")
tm.assert_index_equal(idx, result)
assert result.freq == freq_sample
