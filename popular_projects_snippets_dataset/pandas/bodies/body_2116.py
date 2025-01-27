# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH24763
with tm.assert_produces_warning(warning, match="Could not infer format"):
    res = to_datetime(values, errors="ignore", format=format)
tm.assert_index_equal(res, Index(values))

with tm.assert_produces_warning(warning, match="Could not infer format"):
    res = to_datetime(values, errors="coerce", format=format)
tm.assert_index_equal(res, DatetimeIndex([NaT] * len(values)))

msg = "|".join(
    [
        r'^Given date string "a" not likely a datetime, at position 0$',
        r'^time data "a" doesn\'t match format "%H:%M:%S", at position 0$',
        r'^unconverted data remains: "9", at position 0$',
        r"^second must be in 0..59: 00:01:99, at position 0$",
    ]
)
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(warning, match="Could not infer format"):
        to_datetime(values, errors="raise", format=format)
