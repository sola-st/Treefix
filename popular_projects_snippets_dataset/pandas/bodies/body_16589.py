# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

expected = asof.set_index("time")
trades = trades.set_index("time")
quotes = quotes.set_index("time")

result = merge_asof(
    trades, quotes, left_index=True, right_index=True, by="ticker"
)
tm.assert_frame_equal(result, expected)
