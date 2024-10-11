# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test single integer
result = slice_test_grouped._positional_selector[arg]
expected = slice_test_df.iloc[expected_rows]

tm.assert_frame_equal(result, expected)
