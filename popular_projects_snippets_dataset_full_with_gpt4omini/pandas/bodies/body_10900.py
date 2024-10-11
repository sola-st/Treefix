# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test tuple of ints
result = slice_test_grouped._positional_selector[0, 2, -1]
expected = slice_test_df.iloc[[0, 1, 3, 4, 5, 7]]

tm.assert_frame_equal(result, expected)
