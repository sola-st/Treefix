# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# This setting should be in-place, regardless of whether frame is
#  single-block or multi-block
# GH#304 this used to be incorrectly not-inplace, in which case
#  we needed to ensure _item_cache was cleared.

df = DataFrame(
    {"x": [1.1, 2.1, 3.1, 4.1], "y": [5.1, 6.1, 7.1, 8.1]}, index=[0, 1, 2, 3]
)
df.insert(2, "z", np.nan)
if not using_array_manager:
    if consolidate:
        df._consolidate_inplace()
        assert len(df._mgr.blocks) == 1
    else:
        assert len(df._mgr.blocks) == 2

zvals = df["z"]._values

df.loc[2:, "z"] = 42

expected = Series([np.nan, np.nan, 42, 42], index=df.index, name="z")
tm.assert_series_equal(df["z"], expected)

# check setting occurred in-place
if not using_copy_on_write:
    tm.assert_numpy_array_equal(zvals, expected.values)
    assert np.shares_memory(zvals, df["z"]._values)
