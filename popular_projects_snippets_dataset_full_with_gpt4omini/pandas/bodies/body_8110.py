# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(list("abc"))
result = index.reindex(
    MultiIndex([Index([], np.int64), Index([], np.float64)], [[], []])
)[0]
assert result.levels[0].dtype.type == np.int64
assert result.levels[1].dtype.type == np.float64
