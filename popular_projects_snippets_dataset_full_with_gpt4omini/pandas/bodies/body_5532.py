# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#17690
msg = (
    "Argument 'tzinfo' has incorrect type "
    r"\(expected datetime.tzinfo, got str\)"
)
with pytest.raises(TypeError, match=msg):
    Timestamp("2017-10-22", tzinfo="US/Eastern")

msg = "at most one of"
with pytest.raises(ValueError, match=msg):
    Timestamp("2017-10-22", tzinfo=pytz.utc, tz="UTC")

msg = "Cannot pass a date attribute keyword argument when passing a date string"
with pytest.raises(ValueError, match=msg):
    # GH#5168
    # case where user tries to pass tz as an arg, not kwarg, gets
    # interpreted as `year`
    Timestamp("2012-01-01", "US/Pacific")
