# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

expected = asof
trades.ticker = trades.ticker.astype("category")
quotes.ticker = quotes.ticker.astype("category")
expected.ticker = expected.ticker.astype("category")

result = merge_asof(trades, quotes, on="time", by="ticker")
tm.assert_frame_equal(result, expected)
