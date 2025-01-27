# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_ops.py
# TODO: modify this test when implemented
interval_container = constructor.from_breaks(range(5))
other_container = other_constructor.from_breaks(range(5))
with pytest.raises(NotImplementedError, match="^$"):
    interval_container.overlaps(other_container)
