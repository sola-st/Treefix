# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
dates = [
    datetime(2010, 1, 1, 14),
    datetime(2010, 1, 1, 15),
    datetime(2010, 1, 1, 17),
    datetime(2010, 1, 1, 21),
]

idx = date_range(
    start="2010-01-01 09:00",
    end="2010-02-01 09:00",
    freq="H",
    tz=tz,
    name="idx",
)
expected = DatetimeIndex(dates, freq=None, name="idx", tz=tz)

taken1 = idx.take([5, 6, 8, 12])
taken2 = idx[[5, 6, 8, 12]]

for taken in [taken1, taken2]:
    tm.assert_index_equal(taken, expected)
    assert isinstance(taken, DatetimeIndex)
    assert taken.freq is None
    assert taken.tz == expected.tz
    assert taken.name == expected.name
