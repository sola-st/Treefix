# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
rng = date_range("1/1/2000", periods=10)
idx = Index(["a", "b", "c", "d"])

result = rng.join(idx, how="outer")
assert isinstance(result[0], Timestamp)
