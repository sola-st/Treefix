# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ts = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=tm.makeDateIndex(5))

tm.assert_series_equal(ts, ts.fillna(method="ffill"))

ts[2] = np.NaN

exp = Series([0.0, 1.0, 1.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(method="ffill"), exp)

exp = Series([0.0, 1.0, 3.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(method="backfill"), exp)

exp = Series([0.0, 1.0, 5.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(value=5), exp)

msg = "Must specify a fill 'value' or 'method'"
with pytest.raises(ValueError, match=msg):
    ts.fillna()
