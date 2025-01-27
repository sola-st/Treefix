# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
frame = multiindex_dataframe_random_data

df = frame.T
df["foo", "four"] = "foo"
df = df.sort_index(level=1, axis=1)

stacked = df.stack()
result = df["foo"].stack().sort_index()
tm.assert_series_equal(stacked["foo"], result, check_names=False)
assert result.name is None
assert stacked["bar"].dtype == np.float_
