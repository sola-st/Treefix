# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
cols = Index(list("abc"))
values = np.random.rand(3, 3)
block = new_block(
    values=values.copy(),
    placement=np.arange(3, dtype=np.intp),
    ndim=values.ndim,
)
mgr = BlockManager(blocks=(block,), axes=[cols, Index(np.arange(3))])

tm.assert_almost_equal(mgr.iget(0).internal_values(), values[0])
tm.assert_almost_equal(mgr.iget(1).internal_values(), values[1])
tm.assert_almost_equal(mgr.iget(2).internal_values(), values[2])
