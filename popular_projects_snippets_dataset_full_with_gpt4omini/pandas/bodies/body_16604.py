# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

msg = "allow_exact_matches must be boolean, passed foo"

with pytest.raises(MergeError, match=msg):
    merge_asof(
        trades, quotes, on="time", by="ticker", allow_exact_matches="foo"
    )
