# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 13663
dates = [
    datetime(3000, 1, 1),
    datetime(4000, 1, 1),
    datetime(5000, 1, 1),
    datetime(6000, 1, 1),
]
exp = Index(dates, dtype=object)
# coerces to object
tm.assert_index_equal(Index(dates), exp)

msg = "^Out of bounds nanosecond timestamp: 3000-01-01 00:00:00, at position 0$"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    # can't create DatetimeIndex
    DatetimeIndex(dates)
