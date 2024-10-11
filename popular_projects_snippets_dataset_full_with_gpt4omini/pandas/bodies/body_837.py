# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr("a,b,c: int", item_shape=(3,))

mgr.insert(len(mgr.items), "d", np.array(["foo"] * 3))
mgr.iset(1, np.array(["bar"] * 3))
tm.assert_numpy_array_equal(mgr.iget(0).internal_values(), np.array([0] * 3))
tm.assert_numpy_array_equal(
    mgr.iget(1).internal_values(), np.array(["bar"] * 3, dtype=np.object_)
)
tm.assert_numpy_array_equal(mgr.iget(2).internal_values(), np.array([2] * 3))
tm.assert_numpy_array_equal(
    mgr.iget(3).internal_values(), np.array(["foo"] * 3, dtype=np.object_)
)
