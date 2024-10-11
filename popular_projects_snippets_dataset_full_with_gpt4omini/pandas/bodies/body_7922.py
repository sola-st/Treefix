# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
idx = PeriodIndex(["2011-01", "NaT", "2011-02"], freq="M")
assert idx[0] == Period("2011-01", freq="M")
assert idx[1] is NaT

s = Series([0, 1, 2], index=idx)
assert s[NaT] == 1

s = Series(idx, index=idx)
assert s[Period("2011-01", freq="M")] == Period("2011-01", freq="M")
assert s[NaT] is NaT
