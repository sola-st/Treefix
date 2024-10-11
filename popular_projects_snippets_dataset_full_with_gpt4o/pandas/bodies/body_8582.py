# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH-24753, GH-24739

msg = "with no precision is not allowed"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(["2000"], dtype="datetime64")

msg = "The 'datetime64' dtype has no unit. Please pass in"
with pytest.raises(ValueError, match=msg):
    Index(["2000"], dtype="datetime64")
