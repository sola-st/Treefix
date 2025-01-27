# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ts = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=tm.makeDateIndex(5))
ts[2] = np.NaN
tm.assert_series_equal(ts.bfill(), ts.fillna(method="bfill"))
