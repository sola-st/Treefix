# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
rng = date_range("1/1/2000", periods=5)
result = rng.groupby(rng.day)
assert isinstance(list(result.values())[0][0], Timestamp)
