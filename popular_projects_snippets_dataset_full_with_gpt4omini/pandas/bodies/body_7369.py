# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_join.py
rng = timedelta_range("1 days", periods=10)
idx = Index(["a", "b", "c", "d"])

result = rng.append(idx)
assert isinstance(result[0], Timedelta)

# it works
rng.join(idx, how="outer")
