# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

expected = DataFrame({"A": [111, "bbb", "ccc"], "B": [1, 2, 3]})
df = DataFrame({"A": ["aaa", "bbb", "ccc"], "B": [1, 2, 3]})
df_original = df.copy()

if not using_copy_on_write:
    with pytest.raises(SettingWithCopyError, match=msg):
        df.loc[0]["A"] = 111

if using_copy_on_write:
    # TODO(CoW) can we still warn here?
    df["A"][0] = 111
    tm.assert_frame_equal(df, df_original)
elif not using_array_manager:
    with pytest.raises(SettingWithCopyError, match=msg):
        df["A"][0] = 111

    df.loc[0, "A"] = 111
    tm.assert_frame_equal(df, expected)
else:
    # INFO(ArrayManager) for ArrayManager it doesn't matter that it's
    # a mixed dataframe
    df["A"][0] = 111
    tm.assert_frame_equal(df, expected)
