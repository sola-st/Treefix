# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
result = merge_asof(
    trades, quotes, on="time", by="ticker", tolerance=tolerance_ts
)
expected = tolerance
tm.assert_frame_equal(result, expected)
