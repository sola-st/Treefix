# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
def _compare(old_mgr, new_mgr):
    """compare the blocks, numeric compare ==, object don't"""
    old_blocks = set(old_mgr.blocks)
    new_blocks = set(new_mgr.blocks)
    assert len(old_blocks) == len(new_blocks)

    # compare non-numeric
    for b in old_blocks:
        found = False
        for nb in new_blocks:
            if (b.values == nb.values).all():
                found = True
                break
        assert found

    for b in new_blocks:
        found = False
        for ob in old_blocks:
            if (b.values == ob.values).all():
                found = True
                break
        assert found

        # noops
mgr = create_mgr("f: i8; g: f8")
new_mgr = mgr.convert(copy=True)
_compare(mgr, new_mgr)

# convert
mgr = create_mgr("a,b,foo: object; f: i8; g: f8")
mgr.iset(0, np.array(["1"] * N, dtype=np.object_))
mgr.iset(1, np.array(["2."] * N, dtype=np.object_))
mgr.iset(2, np.array(["foo."] * N, dtype=np.object_))
new_mgr = mgr.convert(copy=True)
assert new_mgr.iget(0).dtype == np.object_
assert new_mgr.iget(1).dtype == np.object_
assert new_mgr.iget(2).dtype == np.object_
assert new_mgr.iget(3).dtype == np.int64
assert new_mgr.iget(4).dtype == np.float64

mgr = create_mgr(
    "a,b,foo: object; f: i4; bool: bool; dt: datetime; i: i8; g: f8; h: f2"
)
mgr.iset(0, np.array(["1"] * N, dtype=np.object_))
mgr.iset(1, np.array(["2."] * N, dtype=np.object_))
mgr.iset(2, np.array(["foo."] * N, dtype=np.object_))
new_mgr = mgr.convert(copy=True)
assert new_mgr.iget(0).dtype == np.object_
assert new_mgr.iget(1).dtype == np.object_
assert new_mgr.iget(2).dtype == np.object_
assert new_mgr.iget(3).dtype == np.int32
assert new_mgr.iget(4).dtype == np.bool_
assert new_mgr.iget(5).dtype.type, np.datetime64
assert new_mgr.iget(6).dtype == np.int64
assert new_mgr.iget(7).dtype == np.float64
assert new_mgr.iget(8).dtype == np.float16
