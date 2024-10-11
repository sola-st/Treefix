# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()
view_original = df[:]
result = df.pop("a")

assert np.shares_memory(result.values, get_array(view_original, "a"))
assert np.shares_memory(get_array(df, "b"), get_array(view_original, "b"))

if using_copy_on_write:
    result.iloc[0] = 0
    assert not np.shares_memory(result.values, get_array(view_original, "a"))
df.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(df, "b"), get_array(view_original, "b"))
    tm.assert_frame_equal(view_original, df_orig)
else:
    expected = DataFrame({"a": [1, 2, 3], "b": [0, 5, 6], "c": [0.1, 0.2, 0.3]})
    tm.assert_frame_equal(view_original, expected)
