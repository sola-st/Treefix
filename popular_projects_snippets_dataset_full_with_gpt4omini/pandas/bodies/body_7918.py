# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
idx1 = period_range("2011-01-01", "2011-01-31", freq="D", name="idx")

for idx in [idx1]:
    result = idx[0]
    assert result == Period("2011-01-01", freq="D")

    result = idx[-1]
    assert result == Period("2011-01-31", freq="D")

    result = idx[0:5]
    expected = period_range("2011-01-01", "2011-01-05", freq="D", name="idx")
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
    assert result.freq == "D"

    result = idx[0:10:2]
    expected = PeriodIndex(
        ["2011-01-01", "2011-01-03", "2011-01-05", "2011-01-07", "2011-01-09"],
        freq="D",
        name="idx",
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
    assert result.freq == "D"

    result = idx[-20:-5:3]
    expected = PeriodIndex(
        ["2011-01-12", "2011-01-15", "2011-01-18", "2011-01-21", "2011-01-24"],
        freq="D",
        name="idx",
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
    assert result.freq == "D"

    result = idx[4::-1]
    expected = PeriodIndex(
        ["2011-01-05", "2011-01-04", "2011-01-03", "2011-01-02", "2011-01-01"],
        freq="D",
        name="idx",
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
    assert result.freq == "D"
