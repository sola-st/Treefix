# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

trades = trades.sort_values("time", ascending=False)
quotes = quotes.sort_values("time", ascending=False)

# we require that we are already sorted on time & quotes
assert not trades.time.is_monotonic_increasing
assert not quotes.time.is_monotonic_increasing
with pytest.raises(ValueError, match="left keys must be sorted"):
    merge_asof(trades, quotes, on="time", by="ticker")

trades = trades.sort_values("time")
assert trades.time.is_monotonic_increasing
assert not quotes.time.is_monotonic_increasing
with pytest.raises(ValueError, match="right keys must be sorted"):
    merge_asof(trades, quotes, on="time", by="ticker")

quotes = quotes.sort_values("time")
assert trades.time.is_monotonic_increasing
assert quotes.time.is_monotonic_increasing

# ok, though has dupes
merge_asof(trades, quotes, on="time", by="ticker")
