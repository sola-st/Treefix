# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_searchsorted.py
pidx = PeriodIndex(
    ["2014-01-01", "2014-01-02", "2014-01-03", "2014-01-04", "2014-01-05"],
    freq=freq,
)

p1 = Period("2014-01-01", freq=freq)
assert pidx.searchsorted(p1) == 0

p2 = Period("2014-01-04", freq=freq)
assert pidx.searchsorted(p2) == 3

assert pidx.searchsorted(NaT) == 5

msg = "Input has different freq=H from PeriodArray"
with pytest.raises(IncompatibleFrequency, match=msg):
    pidx.searchsorted(Period("2014-01-01", freq="H"))

msg = "Input has different freq=5D from PeriodArray"
with pytest.raises(IncompatibleFrequency, match=msg):
    pidx.searchsorted(Period("2014-01-01", freq="5D"))
