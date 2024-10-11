# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# operating on a copy
df = DataFrame(
    {"a": list(range(4)), "b": list("ab.."), "c": ["a", "b", np.nan, "d"]}
)
df_original = df.copy()
mask = pd.isna(df.c)

if using_copy_on_write:
    df[["c"]][mask] = df[["b"]][mask]
    tm.assert_frame_equal(df, df_original)
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        df[["c"]][mask] = df[["b"]][mask]
