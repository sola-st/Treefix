# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH#35132
idx = Index([1, 2, 3], name="x")
idx2 = Index([1, 2, 3, 4], name="x")
expected = Index([1, 2, 3, 4], name="x")
result, _ = idx.reindex(idx2, level="x")
tm.assert_index_equal(result, expected)
