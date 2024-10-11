# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH 16685
# Standard lookup on RangeIndex should not require the engine to be
# created
idx = RangeIndex(2, 10, 3)

assert idx.get_loc(5) == 1
tm.assert_numpy_array_equal(
    idx.get_indexer([2, 8]), ensure_platform_int(np.array([0, 2]))
)
with pytest.raises(KeyError, match="3"):
    idx.get_loc(3)

assert "_engine" not in idx._cache

# Different types of scalars can be excluded immediately, no need to
#  use the _engine
with pytest.raises(KeyError, match="'a'"):
    idx.get_loc("a")

assert "_engine" not in idx._cache
