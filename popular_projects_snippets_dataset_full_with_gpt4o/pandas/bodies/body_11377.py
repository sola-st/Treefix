# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: selecting a single column now also uses Copy-on-Write
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

s = df["a"]

assert np.shares_memory(s.values, get_array(df, "a"))

if using_copy_on_write or using_array_manager:
    s[0] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            s[0] = 0

expected = Series([0, 2, 3], name="a")
tm.assert_series_equal(s, expected)
if using_copy_on_write:
    # assert not np.shares_memory(s.values, get_array(df, "a"))
    tm.assert_frame_equal(df, df_orig)
    # ensure cached series on getitem is not the changed series
    tm.assert_series_equal(df["a"], df_orig["a"])
else:
    df_orig.iloc[0, 0] = 0
    tm.assert_frame_equal(df, df_orig)
