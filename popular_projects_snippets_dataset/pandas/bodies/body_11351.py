# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["foo", "bar", "baz"]})
df_orig = df.copy()

df_replaced = df.replace(**replace_kwargs)

if using_copy_on_write:
    if (df_replaced["b"] == df["b"]).all():
        assert np.shares_memory(get_array(df_replaced, "b"), get_array(df, "b"))
    assert np.shares_memory(get_array(df_replaced, "c"), get_array(df, "c"))

# mutating squeezed df triggers a copy-on-write for that column/block
df_replaced.loc[0, "c"] = -1
if using_copy_on_write:
    assert not np.shares_memory(get_array(df_replaced, "c"), get_array(df, "c"))

if "a" in replace_kwargs["to_replace"]:
    arr = get_array(df_replaced, "a")
    df_replaced.loc[0, "a"] = 100
    assert np.shares_memory(get_array(df_replaced, "a"), arr)
tm.assert_frame_equal(df, df_orig)
