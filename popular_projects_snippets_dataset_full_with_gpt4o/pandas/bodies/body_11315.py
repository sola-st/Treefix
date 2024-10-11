# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame(
    [[1, 2], [3, 4], [5, 6]],
    index=date_range("2020-01-01", "2020-01-03"),
    columns=["a", "b"],
)
df_orig = df.copy()
df_orig.index = date_range("2020-01-02", "2020-01-04")
df2 = df.shift(periods=1, freq="1D")

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))

df.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(df, "a"), get_array(df2, "a"))
tm.assert_frame_equal(df2, df_orig)
