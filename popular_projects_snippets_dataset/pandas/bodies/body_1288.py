# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH#42570
df = DataFrame(np.arange(25).reshape(5, 5))
df_original = df.copy()
chained = df.loc[:3]
with option_context("chained_assignment", "warn"):
    if not using_copy_on_write:
        with tm.assert_produces_warning(SettingWithCopyWarning) as t:
            chained[2] = rhs
            assert t[0].filename == __file__
    else:
        # INFO(CoW) no warning, and original dataframe not changed
        with tm.assert_produces_warning(None):
            chained[2] = rhs
        tm.assert_frame_equal(df, df_original)
