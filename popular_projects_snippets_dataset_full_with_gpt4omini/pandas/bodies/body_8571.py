# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 3746
dti = DatetimeIndex(["2010"], tz="UTC")
msg = "Cannot directly set timezone"
with pytest.raises(AttributeError, match=msg):
    dti.tz = pytz.timezone("US/Pacific")
