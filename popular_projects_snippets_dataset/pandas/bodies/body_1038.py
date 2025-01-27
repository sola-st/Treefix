# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = simple_multiindex_dataframe
arr = df.values
result = df.iloc[2, 2]
expected = arr[2, 2]
assert result == expected
