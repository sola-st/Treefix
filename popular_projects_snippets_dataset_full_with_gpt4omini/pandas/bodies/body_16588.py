# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

expected = asof
quotes = quotes.set_index("time")

result = merge_asof(
    trades, quotes, left_on="time", right_index=True, by="ticker"
)
tm.assert_frame_equal(result, expected)
