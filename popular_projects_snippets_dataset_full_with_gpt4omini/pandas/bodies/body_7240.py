# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH 32413
index = Index([1, np.nan])
cond = index.notna()
other = Index(["a", "b"], dtype="string")

expected = Index([1.0, "b"])
result = index.where(cond, other)

tm.assert_index_equal(result, expected)
