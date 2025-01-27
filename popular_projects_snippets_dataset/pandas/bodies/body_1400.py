# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 3455

df = tm.makeCustomDataframe(10, 3)
df.columns = ["a", "a", "b"]
result = df[["b", "a"]].columns
expected = Index(["b", "a", "a"])
tm.assert_index_equal(result, expected)
