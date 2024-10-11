# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
cop = fblock.copy()
assert cop is not fblock
assert_block_equal(fblock, cop)
