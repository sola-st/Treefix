# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#8058
# ops testing
a = Series(np.random.randn(5), name=0)
b = Series(np.random.randn(5))
b.name = pd.Timestamp("2000-01-01")
tm.assert_series_equal(a / b, 1 / (b / a))
