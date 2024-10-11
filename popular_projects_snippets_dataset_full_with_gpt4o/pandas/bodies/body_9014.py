# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
a = IntIndex(5, np.array([0, 3, 4], dtype=np.int32))
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 2, 3, 4], np.int32))
assert res.equals(exp)

a = IntIndex(5, np.array([], dtype=np.int32))
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 2], np.int32))
assert res.equals(exp)

a = IntIndex(5, np.array([], dtype=np.int32))
b = IntIndex(5, np.array([], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([], np.int32))
assert res.equals(exp)

a = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
b = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 1, 2, 3, 4], np.int32))
assert res.equals(exp)

a = IntIndex(5, np.array([0, 1], dtype=np.int32))
b = IntIndex(4, np.array([0, 1], dtype=np.int32))

msg = "Indices must reference same underlying length"
with pytest.raises(ValueError, match=msg):
    a.make_union(b)
