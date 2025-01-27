# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py

expected = Period("2007-01", freq="M")
i1 = Period("200701", freq="M")
assert i1 == expected

i1 = Period("200701", freq="M")
assert i1 == expected

i1 = Period(200701, freq="M")
assert i1 == expected

i1 = Period(ordinal=200701, freq="M")
assert i1.year == 18695

i1 = Period(datetime(2007, 1, 1), freq="M")
i2 = Period("200701", freq="M")
assert i1 == i2

i1 = Period(date(2007, 1, 1), freq="M")
i2 = Period(datetime(2007, 1, 1), freq="M")
i3 = Period(np.datetime64("2007-01-01"), freq="M")
i4 = Period("2007-01-01 00:00:00", freq="M")
i5 = Period("2007-01-01 00:00:00.000", freq="M")
assert i1 == i2
assert i1 == i3
assert i1 == i4
assert i1 == i5
