# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#13459
with tm.set_timezone(timezone):
    rng = date_range("1/1/2000 9:30", periods=10, freq="D", tz=tzlocal())

    result = rng.normalize()
    expected = date_range("1/1/2000", periods=10, freq="D", tz=tzlocal())
    expected = expected._with_freq(None)
    tm.assert_index_equal(result, expected)

    assert result.is_normalized
    assert not rng.is_normalized
