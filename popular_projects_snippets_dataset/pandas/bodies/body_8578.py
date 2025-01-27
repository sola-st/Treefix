# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 23579
dti = date_range("2016-01-01", periods=3, tz="US/Central")
msg = "data is already tz-aware US/Central, unable to set specified tz"
with pytest.raises(TypeError, match=msg):
    DatetimeIndex(dti, tz="Asia/Tokyo")
