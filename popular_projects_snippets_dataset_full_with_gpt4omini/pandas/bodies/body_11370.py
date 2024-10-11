# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
df_orig = df.copy()

# modify subset -> don't modify parent
subset = df[:].iloc[0].iloc[0:2]
subset.iloc[0] = 0
if using_copy_on_write or using_array_manager:
    tm.assert_frame_equal(df, df_orig)
else:
    assert df.iloc[0, 0] == 0

# modify parent -> don't modify subset
subset = df[:].iloc[0].iloc[0:2]
df.iloc[0, 0] = 0
expected = Series([1, 4], index=["a", "b"], name=0)
if using_copy_on_write or using_array_manager:
    tm.assert_series_equal(subset, expected)
else:
    assert subset.iloc[0] == 0
