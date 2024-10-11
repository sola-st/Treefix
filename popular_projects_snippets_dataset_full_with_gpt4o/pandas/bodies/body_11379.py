# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: selecting a single column (which now also uses Copy-on-Write to protect
# the view) should always give a new object (i.e. not make use of a cache)
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

s1 = method(df)
s2 = method(df)

is_iloc = request.node.callspec.id == "iloc"
if using_copy_on_write or is_iloc:
    assert s1 is not s2
else:
    assert s1 is s2

if using_copy_on_write or using_array_manager:
    s1.iloc[0] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            s1.iloc[0] = 0

if using_copy_on_write:
    tm.assert_series_equal(s2, df_orig["a"])
    tm.assert_frame_equal(df, df_orig)
else:
    assert s2.iloc[0] == 0
