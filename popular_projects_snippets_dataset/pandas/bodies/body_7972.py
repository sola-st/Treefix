# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
year = Series([2001, 2002, 2003])
quarter = year - 2000
idx = PeriodIndex(year=year, quarter=quarter)
strs = [f"{t[0]:d}Q{t[1]:d}" for t in zip(quarter, year)]
lops = list(map(Period, strs))
p = PeriodIndex(lops)
tm.assert_index_equal(p, idx)
