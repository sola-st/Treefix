# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH#41933
ci = CategoricalIndex(["A", "B", np.nan])
res = ci.get_loc(np.nan)

assert res == 2
