# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py

rng = timedelta_range("1 day", periods=5)
result = rng.groupby(rng.days)
assert isinstance(list(result.values())[0][0], Timedelta)
