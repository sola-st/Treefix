# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
dr = date_range(
    start="2013-01-01",
    periods=2,
    freq=offsets.FY5253(startingMonth=1, weekday=3, variation="nearest"),
)
assert dr[0] == Timestamp("2013-01-31")
assert dr[1] == Timestamp("2014-01-30")
