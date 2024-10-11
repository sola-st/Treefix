# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_freq_attr.py
# GH#20678
idx = DatetimeIndex(values, tz=tz)

# can set to an offset, converting from string if necessary
idx._data.freq = freq
assert idx.freq == freq
assert isinstance(idx.freq, DateOffset)

# can reset to None
idx._data.freq = None
assert idx.freq is None
