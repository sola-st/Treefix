# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 31202
idx = simple_index
result = idx.map(str)
expected = Index([str(x) for x in idx], dtype=object)
tm.assert_index_equal(result, expected)
