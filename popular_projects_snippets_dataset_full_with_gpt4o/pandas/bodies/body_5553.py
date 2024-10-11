# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 3746
ts = Timestamp("2010")
msg = "Cannot directly set timezone"
with pytest.raises(AttributeError, match=msg):
    ts.tz = tz
