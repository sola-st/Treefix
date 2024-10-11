# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=3, tz="UTC")

res = dti.astype("M8[s, US/Pacific]")
assert res.dtype == "M8[s, US/Pacific]"

dta = dti._data
res = dta.astype("M8[s, US/Pacific]")
assert res.dtype == "M8[s, US/Pacific]"

# from non-nano to non-nano, preserving reso
res2 = res.astype("M8[s, UTC]")
assert res2.dtype == "M8[s, UTC]"
assert not tm.shares_memory(res2, res)

res3 = res.astype("M8[s, UTC]", copy=False)
assert res2.dtype == "M8[s, UTC]"
assert tm.shares_memory(res3, res)
