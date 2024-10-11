# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# coerce all
mgr = create_mgr("c: f4; d: f2; e: f8")

t = np.dtype(t)
tmgr = mgr.astype(t)
assert tmgr.iget(0).dtype.type == t
assert tmgr.iget(1).dtype.type == t
assert tmgr.iget(2).dtype.type == t

# mixed
mgr = create_mgr("a,b: object; c: bool; d: datetime; e: f4; f: f2; g: f8")

t = np.dtype(t)
tmgr = mgr.astype(t, errors="ignore")
assert tmgr.iget(2).dtype.type == t
assert tmgr.iget(4).dtype.type == t
assert tmgr.iget(5).dtype.type == t
assert tmgr.iget(6).dtype.type == t

assert tmgr.iget(0).dtype.type == np.object_
assert tmgr.iget(1).dtype.type == np.object_
if t != np.int64:
    assert tmgr.iget(3).dtype.type == np.datetime64
else:
    assert tmgr.iget(3).dtype.type == t
