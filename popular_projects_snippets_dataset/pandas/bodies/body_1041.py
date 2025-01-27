# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = multiindex_dataframe_random_data
result = df.iloc[:4]
expected = df[:4]
tm.assert_frame_equal(result, expected)
