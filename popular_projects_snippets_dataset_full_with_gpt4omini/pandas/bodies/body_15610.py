# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#14872

data = Series(
    [NaT, NaT, datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc)]
)

filled = data.fillna(method="bfill")

expected = Series(
    [
        datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc),
        datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc),
        datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc),
    ]
)

tm.assert_series_equal(filled, expected)
