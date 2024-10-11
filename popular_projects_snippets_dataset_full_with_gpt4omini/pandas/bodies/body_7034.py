# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
ci = CategoricalIndex(["a", "b", "c", "d"])
mask = np.array([True, False, True, False])

result = ci.where(mask, 2)
expected = Index(["a", 2, "c", 2], dtype=object)
tm.assert_index_equal(result, expected)

msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    # Test the Categorical method directly
    ci._data._where(mask, 2)
