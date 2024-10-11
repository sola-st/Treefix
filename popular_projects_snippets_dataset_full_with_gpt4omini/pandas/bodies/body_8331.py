# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
rng = date_range("1/1/2000", freq="12min", periods=10)
result = pd.Index(rng).time
expected = [t.time() for t in rng]
assert (result == expected).all()
