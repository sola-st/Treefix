# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
val = Period(freq="A", year=2007)
result1 = val.asfreq("5t")
result2 = val.asfreq("t")
expected = Period("2007-12-31 23:59", freq="t")
assert result1.ordinal == expected.ordinal
assert result1.freqstr == "5T"
assert result2.ordinal == expected.ordinal
assert result2.freqstr == "T"
