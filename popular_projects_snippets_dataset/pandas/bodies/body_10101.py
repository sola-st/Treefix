# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
vals = Series([], dtype=np.float64)

ewm = vals.ewm(3)
result = getattr(ewm, method)()
tm.assert_almost_equal(result, vals)
