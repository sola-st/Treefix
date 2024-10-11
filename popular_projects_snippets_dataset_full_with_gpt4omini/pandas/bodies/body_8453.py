# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
msg = "type object 'DatetimeIndex' has no attribute 'millisecond'"
with pytest.raises(AttributeError, match=msg):
    DatetimeIndex.millisecond

msg = "'DatetimeIndex' object has no attribute 'millisecond'"
with pytest.raises(AttributeError, match=msg):
    DatetimeIndex([]).millisecond
