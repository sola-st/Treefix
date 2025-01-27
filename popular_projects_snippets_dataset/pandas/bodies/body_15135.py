# Extracted from ./data/repos/pandas/pandas/tests/test_aggregation.py
func = {"C": np.mean, "D": {"foo": np.mean, "bar": np.mean}}
result = maybe_mangle_lambdas(func)
assert result == func
