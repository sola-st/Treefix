# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
msg = f"Wrong type {type(start)} for value {start}"
with pytest.raises(TypeError, match=msg):
    RangeIndex(start, stop, step)
