# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_head_tail.py
# test empty dataframe
empty_df = DataFrame()
tm.assert_frame_equal(empty_df.tail(), empty_df)
tm.assert_frame_equal(empty_df.head(), empty_df)
