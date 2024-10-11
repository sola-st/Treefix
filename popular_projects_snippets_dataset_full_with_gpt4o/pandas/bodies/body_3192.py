# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
vals = [np.nan, np.nan, 1, 2, 4, 10, np.nan, np.nan]
obj = frame_or_series(vals)

res = obj.pct_change(periods=periods, fill_method=fill_method, limit=limit)
tm.assert_equal(res, frame_or_series(exp))
