# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
"""right dataframe (multi-indexed) for multi-index join tests"""
df = multiindex_dataframe_random_data
df.index.names = ["key1", "key2"]

df.columns = ["j_one", "j_two", "j_three"]
exit(df)
