# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

# "on" parameter and index together is prohibited
trades = trades.set_index("time")
quotes = quotes.set_index("time")
msg = 'Can only pass argument "left_on" OR "left_index" not both.'
with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades, quotes, left_on="price", left_index=True, right_index=True
    )
