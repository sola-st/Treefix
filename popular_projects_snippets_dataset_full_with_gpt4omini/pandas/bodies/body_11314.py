# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame(
    [[1, 2], [3, 4], [5, 6]],
    index=date_range("2020-01-01", "2020-01-03"),
    columns=["a", "b"],
)
df2 = df.shift(periods=1, axis=0)

assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
