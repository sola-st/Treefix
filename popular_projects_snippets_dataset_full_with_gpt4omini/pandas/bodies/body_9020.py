# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind=kind)
assert idx.lookup(-1) == -1
assert idx.lookup(0) == -1
assert idx.lookup(1) == -1
assert idx.lookup(2) == 0
assert idx.lookup(3) == 1
assert idx.lookup(4) == -1

idx = make_sparse_index(4, np.array([], dtype=np.int32), kind=kind)

for i in range(-1, 5):
    assert idx.lookup(i) == -1

idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind=kind)
assert idx.lookup(-1) == -1
assert idx.lookup(0) == 0
assert idx.lookup(1) == 1
assert idx.lookup(2) == 2
assert idx.lookup(3) == 3
assert idx.lookup(4) == -1

idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind=kind)
assert idx.lookup(-1) == -1
assert idx.lookup(0) == 0
assert idx.lookup(1) == -1
assert idx.lookup(2) == 1
assert idx.lookup(3) == 2
assert idx.lookup(4) == -1
