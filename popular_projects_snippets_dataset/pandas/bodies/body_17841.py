# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# see gh-20503
#
# Test ensures that `tm.assert_frame_equals` raises the right exception
# when comparing DataFrames containing differing unicode objects.
msg = msg.format(obj=obj_fixture)
with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, by_blocks=by_blocks_fixture, obj=obj_fixture)
