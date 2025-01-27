# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
# GH#11838
# naive and tz-aware datetimes

t = Timestamp("2015-12-01 09:30:30")
s = Series([Timestamp("2015-12-01 09:30:00"), Timestamp("2015-12-01 09:31:00")])
result = s.clip(upper=t)
expected = Series(
    [Timestamp("2015-12-01 09:30:00"), Timestamp("2015-12-01 09:30:30")]
)
tm.assert_series_equal(result, expected)

t = Timestamp("2015-12-01 09:30:30", tz="US/Eastern")
s = Series(
    [
        Timestamp("2015-12-01 09:30:00", tz="US/Eastern"),
        Timestamp("2015-12-01 09:31:00", tz="US/Eastern"),
    ]
)
result = s.clip(upper=t)
expected = Series(
    [
        Timestamp("2015-12-01 09:30:00", tz="US/Eastern"),
        Timestamp("2015-12-01 09:30:30", tz="US/Eastern"),
    ]
)
tm.assert_series_equal(result, expected)
