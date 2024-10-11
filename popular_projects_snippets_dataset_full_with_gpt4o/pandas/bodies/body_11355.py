# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a subset of the columns of a DataFrame
# + afterwards modifying the parent
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})

subset = df[["a", "c"]]
if using_copy_on_write:
    # the subset shares memory ...
    assert np.shares_memory(get_array(subset, "a"), get_array(df, "a"))
    # ... but parent uses CoW parent when it is modified
df.iloc[0, 0] = 0

assert not np.shares_memory(get_array(subset, "a"), get_array(df, "a"))
if using_copy_on_write:
    # different column/block still shares memory
    assert np.shares_memory(get_array(subset, "c"), get_array(df, "c"))

expected = DataFrame({"a": [1, 2, 3], "c": [0.1, 0.2, 0.3]})
tm.assert_frame_equal(subset, expected)
