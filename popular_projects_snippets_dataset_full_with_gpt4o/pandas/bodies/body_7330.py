# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
idx1 = timedelta_range("1 day", "31 day", freq="D", name="idx")

for idx in [idx1]:
    result = idx[0]
    assert result == Timedelta("1 day")

    result = idx[0:5]
    expected = timedelta_range("1 day", "5 day", freq="D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[0:10:2]
    expected = timedelta_range("1 day", "9 day", freq="2D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[-20:-5:3]
    expected = timedelta_range("12 day", "24 day", freq="3D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[4::-1]
    expected = TimedeltaIndex(
        ["5 day", "4 day", "3 day", "2 day", "1 day"], freq="-1D", name="idx"
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
