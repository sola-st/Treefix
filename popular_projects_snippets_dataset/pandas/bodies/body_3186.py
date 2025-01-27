# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH 15713
# DataFrame/Series is all nans
result = frame_or_series([np.nan]).asof([0])
expected = frame_or_series([np.nan])
tm.assert_equal(result, expected)
