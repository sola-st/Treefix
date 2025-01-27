# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
msg = "slice step cannot be zero"
with pytest.raises(ValueError, match=msg):
    BlockPlacement(slc)
