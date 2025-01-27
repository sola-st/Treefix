# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(np.random.randn(4, 10), columns=range(0, 20, 2))
original = df.copy()
subset = df.iloc[:, slice(4, 8)]

if not using_array_manager and not using_copy_on_write:
    # verify slice is view
    assert np.shares_memory(df[8]._values, subset[8]._values)

    subset.loc[:, 8] = 0.0

    assert (df[8] == 0).all()

    # with the enforcement of GH#45333 in 2.0, this remains a view
    assert np.shares_memory(df[8]._values, subset[8]._values)
else:
    if using_copy_on_write:
        # verify slice is view
        assert np.shares_memory(df[8]._values, subset[8]._values)
    subset[8] = 0.0
    # subset changed
    assert (subset[8] == 0).all()
    # but df itself did not change (setitem replaces full column)
    tm.assert_frame_equal(df, original)
