# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# normal freq to combined freq
p = Period("2007", freq="H")

# ordinal will not change
expected = Period("2007", freq="25H")
for freq, how in zip(["1D1H", "1H1D"], ["E", "S"]):
    result = p.asfreq(freq, how=how)
    assert result == expected
    assert result.ordinal == expected.ordinal
    assert result.freq == expected.freq

# combined freq to normal freq
p1 = Period(freq="1D1H", year=2007)
p2 = Period(freq="1H1D", year=2007)

# ordinal will change because how=E is the default
result1 = p1.asfreq("H")
result2 = p2.asfreq("H")
expected = Period("2007-01-02", freq="H")
assert result1 == expected
assert result1.ordinal == expected.ordinal
assert result1.freq == expected.freq
assert result2 == expected
assert result2.ordinal == expected.ordinal
assert result2.freq == expected.freq

# ordinal will not change
result1 = p1.asfreq("H", how="S")
result2 = p2.asfreq("H", how="S")
expected = Period("2007-01-01", freq="H")
assert result1 == expected
assert result1.ordinal == expected.ordinal
assert result1.freq == expected.freq
assert result2 == expected
assert result2.ordinal == expected.ordinal
assert result2.freq == expected.freq
