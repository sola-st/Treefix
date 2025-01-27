# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
msg = "iadd causes length change"
with pytest.raises(ValueError, match=msg):
    BlockPlacement(val).add(-10)
