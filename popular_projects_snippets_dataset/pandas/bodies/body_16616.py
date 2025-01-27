# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

result = merge_asof(
    trades,
    quotes,
    on="time",
    by="ticker",
    tolerance=Timedelta("100ms"),
    allow_exact_matches=False,
)
expected = allow_exact_matches_and_tolerance
tm.assert_frame_equal(result, expected)
