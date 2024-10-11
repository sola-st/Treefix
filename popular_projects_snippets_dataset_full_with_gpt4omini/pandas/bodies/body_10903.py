# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test the default as_index behaviour
result = slice_test_df.groupby("Group", sort=False)._positional_selector[arg]
expected = slice_test_df.iloc[expected_rows]

tm.assert_frame_equal(result, expected)
