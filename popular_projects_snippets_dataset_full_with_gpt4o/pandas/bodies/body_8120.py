# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH#30103 method removed for all types except IntervalIndex
if isinstance(index, IntervalIndex):
    index.contains(1)
else:
    msg = f"'{type(index).__name__}' object has no attribute 'contains'"
    with pytest.raises(AttributeError, match=msg):
        index.contains(1)
