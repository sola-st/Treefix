# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# mgr is not consolidated, f8 & f8-2 blocks
mgr = create_mgr("a: f8; b: i8; c: f8; d: i8; e: f8; f: bool; g: f8-2")

reindexed = mgr.reindex_axis(["g", "c", "a", "d"], axis=0)
# reindex_axis does not consolidate_inplace, as that risks failing to
#  invalidate _item_cache
assert not reindexed.is_consolidated()

tm.assert_index_equal(reindexed.items, Index(["g", "c", "a", "d"]))
tm.assert_almost_equal(
    mgr.iget(6).internal_values(), reindexed.iget(0).internal_values()
)
tm.assert_almost_equal(
    mgr.iget(2).internal_values(), reindexed.iget(1).internal_values()
)
tm.assert_almost_equal(
    mgr.iget(0).internal_values(), reindexed.iget(2).internal_values()
)
tm.assert_almost_equal(
    mgr.iget(3).internal_values(), reindexed.iget(3).internal_values()
)
