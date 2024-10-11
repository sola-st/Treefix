# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([5, 4, 3, 2, 1])
with pytest.raises(Exception, match="ascending must be a single bool value or"):
    index.sortlevel(ascending="True")

with pytest.raises(
    Exception, match="ascending must be a list of bool values of length 1"
):
    index.sortlevel(ascending=[True, True])

with pytest.raises(Exception, match="ascending must be a bool value"):
    index.sortlevel(ascending=["True"])

expected = Index([1, 2, 3, 4, 5])
result = index.sortlevel(ascending=[True])
tm.assert_index_equal(result[0], expected)

expected = Index([1, 2, 3, 4, 5])
result = index.sortlevel(ascending=True)
tm.assert_index_equal(result[0], expected)

expected = Index([5, 4, 3, 2, 1])
result = index.sortlevel(ascending=False)
tm.assert_index_equal(result[0], expected)
