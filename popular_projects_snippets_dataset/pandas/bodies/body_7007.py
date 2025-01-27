# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_fillna.py
# We validate the fill value even if fillna is a no-op
ci = CategoricalIndex([2, 3, 3])
cat = ci._data

msg = "Cannot setitem on a Categorical with a new category"
res = ci.fillna(False)
# nothing to fill, so we dont cast
tm.assert_index_equal(res, ci)

# Same check directly on the Categorical
with pytest.raises(TypeError, match=msg):
    cat.fillna(False)
