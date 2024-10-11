# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
newb = fblock.copy()
locs = newb.mgr_locs
nb = newb.delete(0)[0]
assert newb.mgr_locs is locs

assert nb is not newb

tm.assert_numpy_array_equal(
    nb.mgr_locs.as_array, np.array([2, 4], dtype=np.intp)
)
assert not (newb.values[0] == 1).all()
assert (nb.values[0] == 1).all()

newb = fblock.copy()
locs = newb.mgr_locs
nb = newb.delete(1)
assert len(nb) == 2
assert newb.mgr_locs is locs

tm.assert_numpy_array_equal(
    nb[0].mgr_locs.as_array, np.array([0], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    nb[1].mgr_locs.as_array, np.array([4], dtype=np.intp)
)
assert not (newb.values[1] == 2).all()
assert (nb[1].values[0] == 2).all()

newb = fblock.copy()
nb = newb.delete(2)
assert len(nb) == 1
tm.assert_numpy_array_equal(
    nb[0].mgr_locs.as_array, np.array([0, 2], dtype=np.intp)
)
assert (nb[0].values[1] == 1).all()

newb = fblock.copy()

with pytest.raises(IndexError, match=None):
    newb.delete(3)
