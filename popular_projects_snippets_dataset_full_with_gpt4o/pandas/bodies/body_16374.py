# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
d = {("a", "a"): 0.0, ("b", "a"): 1.0, ("b", "c"): 2.0}
_d = sorted(d.items())
result = Series(d)
expected = Series(
    [x[1] for x in _d], index=MultiIndex.from_tuples([x[0] for x in _d])
)
tm.assert_series_equal(result, expected)

d["z"] = 111.0
_d.insert(0, ("z", d["z"]))
result = Series(d)
expected = Series(
    [x[1] for x in _d], index=Index([x[0] for x in _d], tupleize_cols=False)
)
result = result.reindex(index=expected.index)
tm.assert_series_equal(result, expected)
