# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
frame = multiindex_dataframe_random_data

result = frame.unstack("second")
expected = frame.unstack(level=1)
tm.assert_frame_equal(result, expected)
