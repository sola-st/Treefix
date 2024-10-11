# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_functions.py
df = DataFrame({"b": ["a"] * 3})
df2 = DataFrame({"a": ["a"] * 3})
result = concat([df, df2], axis=1)

if using_copy_on_write:
    assert np.shares_memory(get_array(result, "b"), get_array(df, "b"))
    assert np.shares_memory(get_array(result, "a"), get_array(df2, "a"))
else:
    assert not np.shares_memory(get_array(result, "b"), get_array(df, "b"))
    assert not np.shares_memory(get_array(result, "a"), get_array(df2, "a"))

expected = result.copy()
df.iloc[0, 0] = "d"
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "b"), get_array(df, "b"))
    assert np.shares_memory(get_array(result, "a"), get_array(df2, "a"))

df2.iloc[0, 0] = "d"
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, "a"), get_array(df2, "a"))
tm.assert_frame_equal(result, expected)
