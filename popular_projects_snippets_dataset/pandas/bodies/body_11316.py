# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame(
    [[1, 2], [3, 4], [5, 6]], columns=date_range("2020-01-01", "2020-01-02")
)
df2 = df.shift(periods=1, axis=1)

assert np.shares_memory(get_array(df2, "2020-01-02"), get_array(df, "2020-01-01"))
df.iloc[0, 1] = 0
if using_copy_on_write:
    assert not np.shares_memory(
        get_array(df2, "2020-01-02"), get_array(df, "2020-01-01")
    )
expected = DataFrame(
    [[np.nan, 1], [np.nan, 3], [np.nan, 5]],
    columns=date_range("2020-01-01", "2020-01-02"),
)
tm.assert_frame_equal(df2, expected)
