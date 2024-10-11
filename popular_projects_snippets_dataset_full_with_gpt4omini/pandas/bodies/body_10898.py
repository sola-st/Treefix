# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test single slice
result = slice_test_grouped._positional_selector[0:3:2]
expected = slice_test_df.iloc[[0, 1, 4, 5]]

tm.assert_frame_equal(result, expected)
