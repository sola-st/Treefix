# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
result = float_frame.iloc[[1, 4, 7]]
expected = float_frame.loc[float_frame.index[[1, 4, 7]]]
tm.assert_frame_equal(result, expected)

result = float_frame.iloc[:, [2, 0, 1]]
expected = float_frame.loc[:, float_frame.columns[[2, 0, 1]]]
tm.assert_frame_equal(result, expected)
