# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py
# test_map_dictlike generally tests

rng = timedelta_range("1 day", periods=10)

f = lambda x: x.days
result = rng.map(f)
exp = Index([f(x) for x in rng], dtype=np.int32)
tm.assert_index_equal(result, exp)
