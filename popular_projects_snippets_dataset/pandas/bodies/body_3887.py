# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
unstacked1 = df.unstack([column_name])
unstacked2 = df.unstack(column_name)
tm.assert_frame_equal(unstacked1, unstacked2)
