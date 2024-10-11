# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

expected = asof

q = quotes[quotes.ticker != "MSFT"]
result = merge_asof(trades, q, on="time", by="ticker")
expected.loc[expected.ticker == "MSFT", ["bid", "ask"]] = np.nan
tm.assert_frame_equal(result, expected)
