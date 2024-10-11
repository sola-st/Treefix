# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
idx1 = date_range("2011-01-01", "2011-01-31", freq="D", name="idx")
idx2 = date_range(
    "2011-01-01", "2011-01-31", freq="D", tz="Asia/Tokyo", name="idx"
)

for idx in [idx1, idx2]:
    result = idx[0]
    assert result == Timestamp("2011-01-01", tz=idx.tz)

    result = idx[0:5]
    expected = date_range(
        "2011-01-01", "2011-01-05", freq="D", tz=idx.tz, name="idx"
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[0:10:2]
    expected = date_range(
        "2011-01-01", "2011-01-09", freq="2D", tz=idx.tz, name="idx"
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[-20:-5:3]
    expected = date_range(
        "2011-01-12", "2011-01-24", freq="3D", tz=idx.tz, name="idx"
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

    result = idx[4::-1]
    expected = DatetimeIndex(
        ["2011-01-05", "2011-01-04", "2011-01-03", "2011-01-02", "2011-01-01"],
        freq="-1D",
        tz=idx.tz,
        name="idx",
    )
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
