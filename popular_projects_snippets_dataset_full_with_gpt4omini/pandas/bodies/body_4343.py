# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#13896
result = op(frame_or_series(left), frame_or_series(right))
expected = frame_or_series(expected)

tm.assert_equal(result, expected)
