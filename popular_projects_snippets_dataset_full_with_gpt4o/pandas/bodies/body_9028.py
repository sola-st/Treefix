# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
index = BlockIndex(10, [0, 5], [4, 5])
assert index.to_block_index() is index
