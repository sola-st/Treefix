# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
interval = Interval(0, 1)
msg = f"`other` must be an Interval, got {type(other).__name__}"
with pytest.raises(TypeError, match=msg):
    interval.overlaps(other)
