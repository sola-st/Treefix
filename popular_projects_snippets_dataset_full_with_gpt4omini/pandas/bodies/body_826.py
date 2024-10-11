# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
assert fblock.shape == fblock.values.shape
assert fblock.dtype == fblock.values.dtype
assert len(fblock) == len(fblock.values)
