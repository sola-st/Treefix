# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

# MultiIndex is prohibited
trades = trades.set_index("time")
quotes = quotes.set_index(["time", "bid"])
with pytest.raises(MergeError, match="right can only have one index"):
    merge_asof(trades, quotes, left_index=True, right_index=True)
