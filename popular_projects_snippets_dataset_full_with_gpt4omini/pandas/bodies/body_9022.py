# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
bindex = BlockIndex(20, [5, 12], [3, 6])
assert bindex.lookup(idx) == expected

iindex = bindex.to_int_index()
assert iindex.lookup(idx) == expected
