# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# Test for memory errors after internal vector
# reallocations (GH 7157)
# Changed from using np.random.rand to range
# which could cause flaky CI failures when safely_resizes=False
vals = np.array(range(1000), dtype=dtype)

# GH 21688 ensures we can deal with read-only memory views
vals.setflags(write=writable)

# initialise instances; cannot initialise in parametrization,
# as otherwise external views would be held on the array (which is
# one of the things this test is checking)
htable = htable()
uniques = uniques()

# get_labels may append to uniques
htable.get_labels(vals[:nvals], uniques, 0, -1)
# to_array() sets an external_view_exists flag on uniques.
tmp = uniques.to_array()
oldshape = tmp.shape

# subsequent get_labels() calls can no longer append to it
# (except for StringHashTables + ObjectVector)
if safely_resizes:
    htable.get_labels(vals, uniques, 0, -1)
else:
    with pytest.raises(ValueError, match="external reference.*"):
        htable.get_labels(vals, uniques, 0, -1)

uniques.to_array()  # should not raise here
assert tmp.shape == oldshape
