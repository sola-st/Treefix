# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
msg = "Must supply freq for datetime value"
with pytest.raises(ValueError, match=msg):
    Period(datetime.now())
with pytest.raises(ValueError, match=msg):
    Period(datetime.now().date())

msg = "Value must be Period, string, integer, or datetime"
with pytest.raises(ValueError, match=msg):
    Period(1.6, freq="D")
msg = "Ordinal must be an integer"
with pytest.raises(ValueError, match=msg):
    Period(ordinal=1.6, freq="D")
msg = "Only value or ordinal but not both should be given but not both"
with pytest.raises(ValueError, match=msg):
    Period(ordinal=2, value=1, freq="D")

msg = "If value is None, freq cannot be None"
with pytest.raises(ValueError, match=msg):
    Period(month=1)

msg = '^Given date string "-2000" not likely a datetime$'
with pytest.raises(ValueError, match=msg):
    Period("-2000", "A")
msg = "day is out of range for month"
with pytest.raises(DateParseError, match=msg):
    Period("0", "A")
msg = "Unknown datetime string format, unable to parse"
with pytest.raises(DateParseError, match=msg):
    Period("1/1/-2000", "A")
