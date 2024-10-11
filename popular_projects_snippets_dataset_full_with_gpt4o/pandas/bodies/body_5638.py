# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
td = Series([np.timedelta64(10000), NaT], dtype="timedelta64[ns]")
dt = to_datetime(["NaT", "2014-01-01"])

for s in [td, dt]:
    vc = algos.value_counts(s)
    vc_with_na = algos.value_counts(s, dropna=False)
    assert len(vc) == 1
    assert len(vc_with_na) == 2

exp_dt = Series({Timestamp("2014-01-01 00:00:00"): 1})
tm.assert_series_equal(algos.value_counts(dt), exp_dt)
