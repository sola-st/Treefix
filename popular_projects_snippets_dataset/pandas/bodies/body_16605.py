# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

# dti
merge_asof(trades, quotes, on="time", by="ticker", tolerance=Timedelta("1s"))

# integer
merge_asof(
    trades.reset_index(),
    quotes.reset_index(),
    on="index",
    by="ticker",
    tolerance=1,
)

msg = r"incompatible tolerance .*, must be compat with type .*"

# incompat
with pytest.raises(MergeError, match=msg):
    merge_asof(trades, quotes, on="time", by="ticker", tolerance=1)

# invalid
with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades.reset_index(),
        quotes.reset_index(),
        on="index",
        by="ticker",
        tolerance=1.0,
    )

msg = "tolerance must be positive"

# invalid negative
with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades, quotes, on="time", by="ticker", tolerance=-Timedelta("1s")
    )

with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades.reset_index(),
        quotes.reset_index(),
        on="index",
        by="ticker",
        tolerance=-1,
    )
