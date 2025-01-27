# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
frame = multiindex_dataframe_random_data
frame.loc[("bar", "two"), "B"] = 5
assert frame.loc[("bar", "two"), "B"] == 5

# with integer labels
df = frame.copy()
df.columns = list(range(3))
df.loc[("bar", "two"), 1] = 7
assert df.loc[("bar", "two"), 1] == 7
