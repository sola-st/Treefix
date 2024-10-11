# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
years = np.arange(1960, 2000, dtype=np.int64).repeat(4)
quarters = np.tile(np.array([1, 2, 3, 4], dtype=np.int64), 40)

pindex = PeriodIndex(year=years, quarter=quarters)

tm.assert_index_equal(pindex.year, Index(years))
tm.assert_index_equal(pindex.quarter, Index(quarters))
