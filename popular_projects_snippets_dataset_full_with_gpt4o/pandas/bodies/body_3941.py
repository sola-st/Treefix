# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
frame = multiindex_dataframe_random_data

unstacked = frame.unstack("second")
result = unstacked.stack("exp")
expected = frame.unstack().stack(0)
tm.assert_frame_equal(result, expected)

result = frame.stack("exp")
expected = frame.stack()
tm.assert_series_equal(result, expected)
