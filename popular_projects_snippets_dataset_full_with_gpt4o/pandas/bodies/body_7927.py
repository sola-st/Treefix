# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
didx = DatetimeIndex(["2011-01-01", "NaT", "2011-01-03"])
pidx = PeriodIndex(["2011-01-01", "NaT", "2011-01-03"], freq="M")

# check DatetimeIndex compat
for idx in [didx, pidx]:
    assert idx.get_loc(NaT) == 1
    assert idx.get_loc(None) == 1
    assert idx.get_loc(float("nan")) == 1
    assert idx.get_loc(np.nan) == 1
