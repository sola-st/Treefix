# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_copy = df.copy()

# the deep copy doesn't share memory
assert not np.shares_memory(get_array(df_copy, "a"), get_array(df, "a"))
if using_copy_on_write:
    assert df_copy._mgr.refs is None

# mutating copy doesn't mutate original
df_copy.iloc[0, 0] = 0
assert df.iloc[0, 0] == 1
