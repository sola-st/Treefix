# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# Test np ints work

result = slice_test_grouped.nth(np.array([0, 1]))
expected = slice_test_df.iloc[[0, 1, 2, 3, 4]]
tm.assert_frame_equal(result, expected)
