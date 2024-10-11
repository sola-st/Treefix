# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# 24471 non-monotonic
base = TimedeltaIndex(["1 hour", "2 hour", "4 hour", "3 hour"], name="idx")
result = base.intersection(rng, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
assert result.name == expected.name

# if reversed order, frequency is still the same
if all(base == rng[::-1]) and sort is None:
    assert isinstance(result.freq, Hour)
else:
    assert result.freq is None
