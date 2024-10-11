# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#17101
index = Index([], name="idx")
result = DataFrame(columns=["A"], index=index)
result["A"] = []
expected = DataFrame(columns=["A"], index=index)
tm.assert_index_equal(result.index, expected.index)
