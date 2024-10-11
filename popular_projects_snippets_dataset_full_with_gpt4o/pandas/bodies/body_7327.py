# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_freq_attr.py
# GH#20678
idx = TimedeltaIndex(["0 days", "2 days", "4 days"])

# setting with an incompatible freq
msg = (
    "Inferred frequency 2D from passed values does not conform to "
    "passed frequency 5D"
)
with pytest.raises(ValueError, match=msg):
    idx._data.freq = "5D"

# setting with a non-fixed frequency
msg = r"<2 \* BusinessDays> is a non-fixed frequency"
with pytest.raises(ValueError, match=msg):
    idx._data.freq = "2B"

# setting with non-freq string
with pytest.raises(ValueError, match="Invalid frequency"):
    idx._data.freq = "foo"
