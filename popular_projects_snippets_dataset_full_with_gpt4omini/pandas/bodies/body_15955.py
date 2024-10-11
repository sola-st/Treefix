# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nunique.py
# basics.rst doc example
series = Series(np.random.randn(500))
series[20:500] = np.nan
series[10:20] = 5000
result = series.nunique()
assert result == 11
