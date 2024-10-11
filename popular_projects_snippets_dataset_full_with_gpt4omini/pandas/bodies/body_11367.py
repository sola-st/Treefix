# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: creating a subset using multiple, chained getitem calls using views
# still needs to guarantee proper CoW behaviour
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()

# when not using CoW, it depends on whether we have a single block or not
# and whether we are slicing the columns -> in that case we have a view
subset_is_view = request.node.callspec.id in (
    "single-block-column-iloc-slice",
    "single-block-column-loc-slice",
) or (
    request.node.callspec.id
    in ("mixed-block-column-iloc-slice", "mixed-block-column-loc-slice")
    and using_array_manager
)

# modify subset -> don't modify parent
subset = method(df)
subset.iloc[0, 0] = 0
if using_copy_on_write or (not subset_is_view):
    tm.assert_frame_equal(df, df_orig)
else:
    assert df.iloc[0, 0] == 0

# modify parent -> don't modify subset
subset = method(df)
df.iloc[0, 0] = 0
expected = DataFrame({"a": [1, 2], "b": [4, 5]})
if using_copy_on_write or not subset_is_view:
    tm.assert_frame_equal(subset, expected)
else:
    assert subset.iloc[0, 0] == 0
