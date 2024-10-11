# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
df = multiindex_dataframe_random_data

# test setup - check key not in dataframe
with pytest.raises(KeyError, match=r"^\('bar', 'three'\)$"):
    df.loc[("bar", "three"), "B"]

# in theory should be inserting in a sorted space????
df.loc[("bar", "three"), "B"] = 0
expected = 0
result = df.sort_index().loc[("bar", "three"), "B"]
assert result == expected
