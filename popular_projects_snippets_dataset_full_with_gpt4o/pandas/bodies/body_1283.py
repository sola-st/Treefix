# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# from SO:
# https://stackoverflow.com/questions/24054495/potential-bug-setting-value-for-undefined-column-using-iloc
df = DataFrame(np.arange(0, 9), columns=["count"])
df["group"] = "b"
df_original = df.copy()

if using_copy_on_write:
    # TODO(CoW) can we still warn here?
    df.iloc[0:5]["group"] = "a"
    tm.assert_frame_equal(df, df_original)
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        df.iloc[0:5]["group"] = "a"
