# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
frame = multiindex_dataframe_random_data

result = frame.drop(["bar", "qux"], level="first")
expected = frame.iloc[[0, 1, 2, 5, 6]]
tm.assert_frame_equal(result, expected)

result = frame.drop(["two"], level="second")
expected = frame.iloc[[0, 2, 3, 6, 7, 9]]
tm.assert_frame_equal(result, expected)

result = frame.T.drop(["bar", "qux"], axis=1, level="first")
expected = frame.iloc[[0, 1, 2, 5, 6]].T
tm.assert_frame_equal(result, expected)

result = frame.T.drop(["two"], axis=1, level="second")
expected = frame.iloc[[0, 2, 3, 6, 7, 9]].T
tm.assert_frame_equal(result, expected)
