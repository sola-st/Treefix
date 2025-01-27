# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

# GH14253
expected = asof

result = merge_asof(
    trades, quotes, on="time", left_by="ticker", right_by="ticker"
)
tm.assert_frame_equal(result, expected)
