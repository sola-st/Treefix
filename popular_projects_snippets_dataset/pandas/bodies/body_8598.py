# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Test for #25057
# pytz doesn't support fold. Check that we raise
# if fold is passed with pytz
msg = "pytz timezones do not support fold. Please use dateutil timezones."
tz = pytz.timezone("Europe/London")
with pytest.raises(ValueError, match=msg):
    Timestamp(datetime(2019, 10, 27, 0, 30, 0, 0), tz=tz, fold=0)
