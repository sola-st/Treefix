# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

msg = r"incompatible merge keys \[1\] .* must be the same type"

with pytest.raises(MergeError, match=msg):
    merge_asof(trades, quotes, left_on="time", right_on="bid", by="ticker")

with pytest.raises(MergeError, match="can only asof on a key for left"):
    merge_asof(trades, quotes, on=["time", "ticker"], by="ticker")

with pytest.raises(MergeError, match="can only asof on a key for left"):
    merge_asof(trades, quotes, by="ticker")
