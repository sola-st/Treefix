# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_ops.py
interval_container = constructor.from_breaks(range(5))
msg = f"`other` must be Interval-like, got {type(other).__name__}"
with pytest.raises(TypeError, match=msg):
    interval_container.overlaps(other)
