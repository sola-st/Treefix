# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
result1 = Period("1989", freq="2A")
result2 = Period("1989", freq="A")
assert result1.ordinal == result2.ordinal
assert result1.freqstr == "2A-DEC"
assert result2.freqstr == "A-DEC"
assert result1.freq == offsets.YearEnd(2)
assert result2.freq == offsets.YearEnd()

assert (result1 + 1).ordinal == result1.ordinal + 2
assert (1 + result1).ordinal == result1.ordinal + 2
assert (result1 - 1).ordinal == result2.ordinal - 2
assert (-1 + result1).ordinal == result2.ordinal - 2
