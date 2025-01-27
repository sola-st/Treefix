# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr.iset(mgr.items.get_loc("f"), np.random.randn(N))
mgr.iset(mgr.items.get_loc("d"), np.random.randn(N))
mgr.iset(mgr.items.get_loc("b"), np.random.randn(N))
mgr.iset(mgr.items.get_loc("g"), np.random.randn(N))
mgr.iset(mgr.items.get_loc("h"), np.random.randn(N))

# we have datetime/tz blocks in mgr
cons = mgr.consolidate()
assert cons.nblocks == 4
cons = mgr.consolidate().get_numeric_data()
assert cons.nblocks == 1
assert isinstance(cons.blocks[0].mgr_locs, BlockPlacement)
tm.assert_numpy_array_equal(
    cons.blocks[0].mgr_locs.as_array, np.arange(len(cons.items), dtype=np.intp)
)
