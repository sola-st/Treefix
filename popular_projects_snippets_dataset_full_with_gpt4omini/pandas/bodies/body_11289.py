# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_util.py
df = DataFrame({"a": [1, 2, 3]})
assert np.shares_memory(get_array(df, "a"), get_array(df, "a"))
