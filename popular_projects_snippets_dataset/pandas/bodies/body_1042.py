# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = multiindex_dataframe_random_data
df.iloc[:4] = 0

assert (df.values[:4] == 0).all()
assert (df.values[4:] != 0).all()
