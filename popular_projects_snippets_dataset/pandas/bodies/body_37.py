# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 35964
if axis in (0, "index"):
    e = float_frame.columns[0]
    expected = float_frame[[e]].transform(np.abs)
else:
    e = float_frame.index[0]
    expected = float_frame.iloc[[0]].transform(np.abs)
result = float_frame.transform(box({e: np.abs}), axis=axis)
tm.assert_frame_equal(result, expected)
