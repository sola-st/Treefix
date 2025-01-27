# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
# GH #10174

# interpolation = linear (default case)
q = Series([1, 3, 4]).quantile(0.5, interpolation="lower")
assert q == np.percentile(np.array([1, 3, 4]), 50)
assert is_integer(q)

q = Series([1, 3, 4]).quantile(0.5, interpolation="higher")
assert q == np.percentile(np.array([1, 3, 4]), 50)
assert is_integer(q)
