# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
f = (
    lambda x: x[x.ticker == "MSFT"]
    .drop("ticker", axis=1)
    .reset_index(drop=True)
)

# just use a single ticker
expected = f(asof)
trades = f(trades)
quotes = f(quotes)

result = merge_asof(trades, quotes, on="time")
tm.assert_frame_equal(result, expected)
