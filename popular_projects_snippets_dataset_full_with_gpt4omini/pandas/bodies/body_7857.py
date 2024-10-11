# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
years = np.arange(1960, 2000).repeat(4)
quarters = np.tile(list(range(1, 5)), 40)

pindex = PeriodIndex(year=years, quarter=quarters)

stamps = pindex.to_timestamp("D", "end")
expected = DatetimeIndex([x.to_timestamp("D", "end") for x in pindex])
tm.assert_index_equal(stamps, expected)
assert stamps.freq == expected.freq
