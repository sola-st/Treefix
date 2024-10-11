# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: creating a subset using multiple, chained getitem calls using views
# still needs to guarantee proper CoW behaviour
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()

# modify subset -> don't modify parent
subset = df[:]["a"][0:2]
df._clear_item_cache()
subset.iloc[0] = 0
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    assert df.iloc[0, 0] == 0

# modify parent -> don't modify subset
subset = df[:]["a"][0:2]
df._clear_item_cache()
df.iloc[0, 0] = 0
expected = Series([1, 2], name="a")
if using_copy_on_write:
    tm.assert_series_equal(subset, expected)
else:
    assert subset.iloc[0] == 0
