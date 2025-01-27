# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
trades = trades.set_index("time")
quotes = quotes.set_index("time")
msg = 'Can only pass argument "right_on" OR "right_index" not both.'
with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades, quotes, right_on="bid", left_index=True, right_index=True
    )
