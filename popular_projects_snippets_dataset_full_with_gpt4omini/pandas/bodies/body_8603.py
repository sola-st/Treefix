# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_map.py
rng = date_range("1/1/2000", periods=10)

f = lambda x: x.strftime("%Y%m%d")
result = rng.map(f)
exp = Index([f(x) for x in rng], dtype="<U8")
tm.assert_index_equal(result, exp)
