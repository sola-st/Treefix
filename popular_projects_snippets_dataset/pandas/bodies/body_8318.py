# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng = date_range("1/1/2000", "1/1/2002", name="idx", tz=tz)

result = rng[:50].union(rng[50:100])
assert result.name == rng.name
assert result.freq == rng.freq
assert result.tz == rng.tz

result = rng[:50].union(rng[30:100])
assert result.name == rng.name
assert result.freq == rng.freq
assert result.tz == rng.tz

result = rng[:50].union(rng[60:100])
assert result.name == rng.name
assert result.freq is None
assert result.tz == rng.tz

result = rng[:50].intersection(rng[25:75])
assert result.name == rng.name
assert result.freqstr == "D"
assert result.tz == rng.tz

nofreq = DatetimeIndex(list(rng[25:75]), name="other")
result = rng[:50].union(nofreq)
assert result.name is None
assert result.freq == rng.freq
assert result.tz == rng.tz

result = rng[:50].intersection(nofreq)
assert result.name is None
assert result.freq == rng.freq
assert result.tz == rng.tz
