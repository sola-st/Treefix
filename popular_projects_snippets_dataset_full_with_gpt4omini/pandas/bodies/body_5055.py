# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
msg = "invalid option for 'closed': foo"
with pytest.raises(ValueError, match=msg):
    Interval(0, 1, closed="foo")

msg = "left side of interval must be <= right side"
with pytest.raises(ValueError, match=msg):
    Interval(1, 0)
