# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
rng = period_range("1/1/2000", periods=20, freq="D")
periods = list(rng)

result = Index(periods)
assert isinstance(result, PeriodIndex)
