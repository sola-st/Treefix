# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH 15314
freq = "H"
tg = Grouper(freq=freq, convention="start")
grouped = series.groupby(tg)
resampled = series.resample(freq)
for (rk, rv), (gk, gv) in zip(resampled, grouped):
    assert rk == gk
    tm.assert_series_equal(rv, gv)
