# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_fillna.py
# GH#11343
idx = CategoricalIndex([1.0, np.nan, 3.0, 1.0], name="x")
# fill by value in categories
exp = CategoricalIndex([1.0, 1.0, 3.0, 1.0], name="x")
tm.assert_index_equal(idx.fillna(1.0), exp)

cat = idx._data

# fill by value not in categories raises TypeError on EA, casts on CI
msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    cat.fillna(2.0)

result = idx.fillna(2.0)
expected = idx.astype(object).fillna(2.0)
tm.assert_index_equal(result, expected)
