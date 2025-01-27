# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = simple_multiindex_dataframe
result = df.iloc[[0, 1]]
expected = df.xs(4, drop_level=False)
tm.assert_frame_equal(result, expected)
