# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# Test index notation     GH #44688

result = slice_test_grouped.nth[0, 1, -2:]
equivalent = slice_test_grouped.nth([0, 1, slice(-2, None)])
expected = slice_test_df.iloc[[0, 1, 2, 3, 4, 6, 7]]

tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(equivalent, expected)
