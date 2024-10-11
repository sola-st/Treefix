# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_freq_attr.py
# GH#20678
idx = DatetimeIndex(["20180101", "20180103", "20180105"])

# setting with an incompatible freq
msg = (
    "Inferred frequency 2D from passed values does not conform to "
    "passed frequency 5D"
)
with pytest.raises(ValueError, match=msg):
    idx._data.freq = "5D"

# setting with non-freq string
with pytest.raises(ValueError, match="Invalid frequency"):
    idx._data.freq = "foo"
