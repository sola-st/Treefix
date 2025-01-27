# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr.insert(len(mgr.items), "baz", np.zeros(N, dtype=bool))

mgr.iset(mgr.items.get_loc("baz"), np.repeat("foo", N))
idx = mgr.items.get_loc("baz")
assert mgr.iget(idx).dtype == np.object_

mgr2 = mgr.consolidate()
mgr2.iset(mgr2.items.get_loc("baz"), np.repeat("foo", N))
idx = mgr2.items.get_loc("baz")
assert mgr2.iget(idx).dtype == np.object_

mgr2.insert(len(mgr2.items), "quux", np.random.randn(N).astype(int))
idx = mgr2.items.get_loc("quux")
assert mgr2.iget(idx).dtype == np.int_

mgr2.iset(mgr2.items.get_loc("quux"), np.random.randn(N))
assert mgr2.iget(idx).dtype == np.float_
