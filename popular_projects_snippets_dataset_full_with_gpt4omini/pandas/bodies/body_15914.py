# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
# see gh-10174

# interpolation = linear (default case)
q = datetime_series.quantile(0.1, interpolation="linear")
assert q == np.percentile(datetime_series.dropna(), 10)
q1 = datetime_series.quantile(0.1)
assert q1 == np.percentile(datetime_series.dropna(), 10)

# test with and without interpolation keyword
assert q == q1
