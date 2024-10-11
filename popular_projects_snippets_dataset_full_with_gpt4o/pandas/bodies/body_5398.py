# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
tz = tz_aware_fixture
# GH#14621, GH#7825
ts = Timestamp("2016-01-01 09:00:00.000000123", tz=tz)
msg = "value must be an integer, received <class 'float'> for hour"
with pytest.raises(ValueError, match=msg):
    ts.replace(hour=0.1)
