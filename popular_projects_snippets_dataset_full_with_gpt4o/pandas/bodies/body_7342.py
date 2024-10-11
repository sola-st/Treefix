# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tds = ["1day 02:00:00", "1 day 04:00:00", "1 day 10:00:00"]
idx = timedelta_range(start="1d", end="2d", freq="H", name="idx")
expected = TimedeltaIndex(tds, freq=None, name="idx")

taken1 = idx.take([2, 4, 10])
taken2 = idx[[2, 4, 10]]

for taken in [taken1, taken2]:
    tm.assert_index_equal(taken, expected)
    assert isinstance(taken, TimedeltaIndex)
    assert taken.freq is None
    assert taken.name == expected.name
