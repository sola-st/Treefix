# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
tm.assert_frame_equal(x, x.sort_values(by=sort_column))
