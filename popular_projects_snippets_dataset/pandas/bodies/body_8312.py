# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH 4690 (with tz)
base = date_range("6/1/2000", "6/30/2000", freq="D", name="idx")

# if target has the same name, it is preserved
rng2 = date_range("5/15/2000", "6/20/2000", freq="D", name="idx")
expected2 = date_range("6/1/2000", "6/20/2000", freq="D", name="idx")

# if target name is different, it will be reset
rng3 = date_range("5/15/2000", "6/20/2000", freq="D", name="other")
expected3 = date_range("6/1/2000", "6/20/2000", freq="D", name=None)

rng4 = date_range("7/1/2000", "7/31/2000", freq="D", name="idx")
expected4 = DatetimeIndex([], freq="D", name="idx")

for (rng, expected) in [
    (rng2, expected2),
    (rng3, expected3),
    (rng4, expected4),
]:
    result = base.intersection(rng)
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq

# non-monotonic
base = DatetimeIndex(
    ["2011-01-05", "2011-01-04", "2011-01-02", "2011-01-03"], tz=tz, name="idx"
)

rng2 = DatetimeIndex(
    ["2011-01-04", "2011-01-02", "2011-02-02", "2011-02-03"], tz=tz, name="idx"
)
expected2 = DatetimeIndex(["2011-01-04", "2011-01-02"], tz=tz, name="idx")

rng3 = DatetimeIndex(
    ["2011-01-04", "2011-01-02", "2011-02-02", "2011-02-03"],
    tz=tz,
    name="other",
)
expected3 = DatetimeIndex(["2011-01-04", "2011-01-02"], tz=tz, name=None)

# GH 7880
rng4 = date_range("7/1/2000", "7/31/2000", freq="D", tz=tz, name="idx")
expected4 = DatetimeIndex([], tz=tz, name="idx")
assert expected4.freq is None

for (rng, expected) in [
    (rng2, expected2),
    (rng3, expected3),
    (rng4, expected4),
]:
    result = base.intersection(rng, sort=sort)
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)
    assert result.freq == expected.freq
