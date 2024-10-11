# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
int32block = create_block("i4", [0])
assert int32block.dtype == np.int32
