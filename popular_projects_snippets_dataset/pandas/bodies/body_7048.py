# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_map.py
# GH 12756
a = Index([1, 2, 3, 4])
b = Series(["even", "odd", "even", "odd"], dtype="category")
c = Series(["even", "odd", "even", "odd"])

exp = CategoricalIndex(["odd", "even", "odd", np.nan])
tm.assert_index_equal(a.map(b), exp)
exp = Index(["odd", "even", "odd", np.nan])
tm.assert_index_equal(a.map(c), exp)
