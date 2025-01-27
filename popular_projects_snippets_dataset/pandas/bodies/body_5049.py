# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# GH 23013
msg = "Only numeric, Timestamp and Timedelta endpoints are allowed"
with pytest.raises(ValueError, match=msg):
    Interval(left, right)
