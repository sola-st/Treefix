# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: selecting a single column now also uses Copy-on-Write -> when
# setting a value causes an upcast, we don't need to update the parent
# DataFrame through the cache mechanism
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

s = df["a"]
if using_copy_on_write or using_array_manager:
    s[0] = "foo"
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            s[0] = "foo"

expected = Series(["foo", 2, 3], dtype=object, name="a")
tm.assert_series_equal(s, expected)
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
    # ensure cached series on getitem is not the changed series
    tm.assert_series_equal(df["a"], df_orig["a"])
else:
    df_orig["a"] = expected
    tm.assert_frame_equal(df, df_orig)
