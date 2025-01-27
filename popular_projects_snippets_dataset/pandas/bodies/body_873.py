# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
msg = "unbounded slice"
with pytest.raises(ValueError, match=msg):
    BlockPlacement(slc)
