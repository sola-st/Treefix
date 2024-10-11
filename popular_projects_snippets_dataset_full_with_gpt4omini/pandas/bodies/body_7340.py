# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# GH 10295
idx1 = timedelta_range("1 day", "31 day", freq="D", name="idx")

for idx in [idx1]:
    result = idx.take([0])
    assert result == Timedelta("1 day")

    result = idx.take([-1])
    assert result == Timedelta("31 day")

    result = idx.take([0, 1, 2])
    expected = timedelta_range("1 day", "3 day", freq="D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx.take([0, 2, 4])
    expected = timedelta_range("1 day", "5 day", freq="2D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx.take([7, 4, 1])
    expected = timedelta_range("8 day", "2 day", freq="-3D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx.take([3, 2, 5])
    expected = TimedeltaIndex(["4 day", "3 day", "6 day"], name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq is None

    result = idx.take([-3, 2, 5])
    expected = TimedeltaIndex(["29 day", "3 day", "6 day"], name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq is None
