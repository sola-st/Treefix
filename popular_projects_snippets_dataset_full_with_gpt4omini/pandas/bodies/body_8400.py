# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 20854
pre_dst = Timestamp("2010-11-07 01:00:00").tz_localize(
    "US/Pacific", ambiguous=True
)
pst_dst = Timestamp("2010-11-07 01:00:00").tz_localize(
    "US/Pacific", ambiguous=False
)
expect_data = [
    Timestamp("2010-11-07 00:00:00", tz="US/Pacific"),
    pre_dst,
    pst_dst,
]
expected = DatetimeIndex(expect_data, freq="H")
result = date_range(start="2010-11-7", periods=3, freq="H", tz="US/Pacific")
tm.assert_index_equal(result, expected)
