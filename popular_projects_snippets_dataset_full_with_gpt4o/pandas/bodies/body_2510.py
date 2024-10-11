# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#41062
df = DataFrame([[1, 2, 3, 4]], columns=[frozenset(["KEY"]), "B", "C", "C"])
result = df[frozenset(["KEY"])]
expected = Series([1], name=frozenset(["KEY"]))
tm.assert_series_equal(result, expected)
