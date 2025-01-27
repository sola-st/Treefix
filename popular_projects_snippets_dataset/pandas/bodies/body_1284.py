# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# Mixed type setting but same dtype & changing dtype
df = DataFrame(
    {
        "A": date_range("20130101", periods=5),
        "B": np.random.randn(5),
        "C": np.arange(5, dtype="int64"),
        "D": ["a", "b", "c", "d", "e"],
    }
)
df_original = df.copy()

if using_copy_on_write:
    df.loc[2]["D"] = "foo"
    df.loc[2]["C"] = "foo"
    df["C"][2] = "foo"
    tm.assert_frame_equal(df, df_original)

if not using_copy_on_write:
    with pytest.raises(SettingWithCopyError, match=msg):
        df.loc[2]["D"] = "foo"

    with pytest.raises(SettingWithCopyError, match=msg):
        df.loc[2]["C"] = "foo"

    if not using_array_manager:
        with pytest.raises(SettingWithCopyError, match=msg):
            df["C"][2] = "foo"
    else:
        # INFO(ArrayManager) for ArrayManager it doesn't matter if it's
        # changing the dtype or not
        df["C"][2] = "foo"
        assert df.loc[2, "C"] == "foo"
