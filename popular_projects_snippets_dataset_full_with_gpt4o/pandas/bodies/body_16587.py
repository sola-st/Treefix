# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

# GH14253
expected = asof
trades = trades.set_index("time")

result = merge_asof(
    trades, quotes, left_index=True, right_on="time", by="ticker"
)
# left-only index uses right"s index, oddly
expected.index = result.index
# time column appears after left"s columns
expected = expected[result.columns]
tm.assert_frame_equal(result, expected)
