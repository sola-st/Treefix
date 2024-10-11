# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# GH 4690 (with tz)
base = timedelta_range("1 day", periods=4, freq="h", name="idx")
result = base.intersection(rng, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freq == expected.freq
