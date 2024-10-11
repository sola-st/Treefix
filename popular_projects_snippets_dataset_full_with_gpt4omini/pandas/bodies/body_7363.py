# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH-24753, GH-24739

msg = "with no precision is not allowed"
with pytest.raises(ValueError, match=msg):
    TimedeltaIndex(["2000"], dtype="timedelta64")

msg = "The 'timedelta64' dtype has no unit. Please pass in"
with pytest.raises(ValueError, match=msg):
    pd.Index(["2000"], dtype="timedelta64")
