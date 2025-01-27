# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# ravel
s = Series(np.random.randn(10))
tm.assert_almost_equal(s.ravel(order="F"), s.values.ravel(order="F"))
