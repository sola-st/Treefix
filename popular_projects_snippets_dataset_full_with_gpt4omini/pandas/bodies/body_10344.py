# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# Test slices     GH #42947

result = slice_test_grouped.nth[arg]
equivalent = slice_test_grouped.nth(arg)
expected = slice_test_df.iloc[expected_rows]

tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(equivalent, expected)
