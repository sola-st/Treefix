# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 15135
expected = tolerance.set_index("time")
trades = trades.set_index("time")
quotes = quotes.set_index("time")

result = merge_asof(
    trades,
    quotes,
    left_index=True,
    right_index=True,
    by="ticker",
    tolerance=Timedelta("1day"),
)
tm.assert_frame_equal(result, expected)
