# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# test with the chaining
df = DataFrame(
    {
        "A": Series(range(2), dtype="int64"),
        "B": np.array(np.arange(2, 4), dtype=np.float64),
    }
)
df_original = df.copy()
assert df._is_copy is None

if using_copy_on_write:
    df["A"][0] = -5
    df["A"][1] = -6
    tm.assert_frame_equal(df, df_original)
elif not using_array_manager:
    with pytest.raises(SettingWithCopyError, match=msg):
        df["A"][0] = -5

    with pytest.raises(SettingWithCopyError, match=msg):
        df["A"][1] = np.nan

    assert df["A"]._is_copy is None
else:
    # INFO(ArrayManager) for ArrayManager it doesn't matter that it's
    # a mixed dataframe
    df["A"][0] = -5
    df["A"][1] = -6
    expected = DataFrame([[-5, 2], [-6, 3]], columns=list("AB"))
    expected["B"] = expected["B"].astype("float64")
    tm.assert_frame_equal(df, expected)
