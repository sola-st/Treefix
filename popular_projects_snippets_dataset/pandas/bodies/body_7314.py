# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
# GH#10939
# test index
rng = timedelta_range("1 days, 10:11:12.100123456", periods=2, freq="s")
expt = [
    1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1e9,
    1 * 86400 + 10 * 3600 + 11 * 60 + 13 + 100123456.0 / 1e9,
]
tm.assert_almost_equal(rng.total_seconds(), Index(expt))

# test Series
ser = Series(rng)
s_expt = Series(expt, index=[0, 1])
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)

# with nat
ser[1] = np.nan
s_expt = Series(
    [1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1e9, np.nan],
    index=[0, 1],
)
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)
